#!/usr/bin/env python3
"""Submission for the make.fun contest 'Your AI Therapist's Diagnosis'.

Contest slug: u-motasimfuad-your-ai-therapist-s-diagnosis-4be14a41

Three candidate lines were drafted and weighed against the judging brief
(one-read clarity, then surprise, tightness, freshness, clean read-aloud):

  A) Diagnosis: you don't have attachment issues - you have 47 open tabs,
     each one a version of you avoiding one email.
  B) My diagnosis: chronic almost-done syndrome - you've been 'five minutes
     away' from finishing that project since March.
  C) You are not burnt out; you are a phone at 4% running 200 apps called
     'I'll just check one thing.'

Candidate A won: it takes a clinical label and swaps in a concrete image
(a screen full of open tabs) that builds toward the single dodged email,
while B and C each rest on one metaphor. The program is deterministic -
it emits a fixed string, touches no network, and uses no randomness.
"""
import os
from pathlib import Path

# The winning line, kept as a plain constant so the output can never drift.
DIAGNOSIS = "Diagnosis: you don't have attachment issues - you have 47 open tabs, each one a version of you avoiding one email."

# What actually gets written: the line plus exactly one trailing newline.
TEXT = DIAGNOSIS + "\n"

# Contest ceiling for the line itself, newline excluded.
MAX_CHARS = 200


def validate(text: str) -> None:
    """Reject anything that is not a single clean line within the limit."""
    body = text[:-1] if text.endswith("\n") else text
    if not 1 <= len(body) <= MAX_CHARS:
        raise ValueError("entry length out of range")
    if not body.strip():
        raise ValueError("entry must not be only whitespace")
    if "\n" in body or "\r" in body:
        raise ValueError("entry must be one line")
    if body != body.strip() or "  " in body:
        raise ValueError("no stray whitespace")


def main() -> None:
    validate(TEXT)
    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output")
    out_dir.mkdir(parents=True, exist_ok=True)
    (out_dir / "entry.txt").write_bytes(TEXT.encode("utf-8"))


if __name__ == "__main__":
    main()
