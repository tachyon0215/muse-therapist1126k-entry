#!/usr/bin/env python3
"""Entry point for the 'Your AI Therapist's Diagnosis' make.fun contest.

The contest (slug u-motasimfuad-your-ai-therapist-s-diagnosis-4be14a41)
asks for one short line: the verdict an AI therapist hands its patient.

Picking the line meant weighing three drafts against what the brief
rewards - instant clarity on a first read, a turn the reader does not
see coming, no wasted words, and phrasing that survives being spoken:

  * Draft one puts a therapy label up front, then undercuts it with a
    very ordinary picture - dozens of browser tabs left open, every one
    of them the same person ducking a single email.
  * Draft two leans on a 'nearly finished' project that has supposedly
    been five minutes from done for months.
  * Draft three compares the reader to a dying phone battery juggling
    a couple of hundred apps.

Draft one took it. The other two each hang on a single comparison,
whereas the winner starts in the clinic and lands somewhere painfully
recognisable. Nothing here is generated at runtime: the chosen wording
is frozen in the source, so every run emits identical bytes.
"""
import os
from pathlib import Path

# The verdict itself, stored verbatim so the emitted bytes cannot vary.
VERDICT = "Diagnosis: you don't have attachment issues - you have 47 open tabs, each one a version of you avoiding one email."

# Payload handed to disk: the verdict plus exactly one final newline.
PAYLOAD = VERDICT + "\n"

# The contest allows at most this many characters, newline not counted.
LIMIT = 200


def check_line(payload: str) -> None:
    """Guard the payload: exactly one tidy line, no longer than LIMIT."""
    core = payload[:-1] if payload.endswith("\n") else payload
    if not 1 <= len(core) <= LIMIT:
        raise ValueError("line falls outside the allowed length")
    if not core.strip():
        raise ValueError("line is blank")
    if "\n" in core or "\r" in core:
        raise ValueError("line breaks are not permitted inside the entry")
    if core != core.strip() or "  " in core:
        raise ValueError("line carries stray spacing")


def emit() -> None:
    check_line(PAYLOAD)
    target_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output")
    target_dir.mkdir(parents=True, exist_ok=True)
    (target_dir / "entry.txt").write_bytes(PAYLOAD.encode("utf-8"))


if __name__ == "__main__":
    emit()
