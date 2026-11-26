#!/usr/bin/env python3
"""Entry for 'Your AI Therapist's Diagnosis' (u-motasimfuad-your-ai-therapist-s-diagnosis-4be14a41).

Candidates:
  A) "Diagnosis: you don't have attachment issues - you have 47 open tabs, each one a version of you avoiding one email."
  B) "My diagnosis: chronic almost-done syndrome - you've been 'five minutes away' from finishing that project since March."
  C) "You are not burnt out; you are a phone at 4% running 200 apps called 'I'll just check one thing.'"
Selected: "Diagnosis: you don't have attachment issues - you have 47 open tabs, each one a version of you avoiding one email."
Reason: Clinical term flipped into a concrete tab image that escalates to the avoided email; B/C are single metaphors.
Deterministic: fixed text, no network, no randomness.
"""
import os
from pathlib import Path
LINE = "Diagnosis: you don't have attachment issues - you have 47 open tabs, each one a version of you avoiding one email."
TEXT = LINE + "\n"
MAX_CHARS = 200
def validate(text: str) -> None:
    body = text[:-1] if text.endswith("\n") else text
    if not (1 <= len(body) <= MAX_CHARS):
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
