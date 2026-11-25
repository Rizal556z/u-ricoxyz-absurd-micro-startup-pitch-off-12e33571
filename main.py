#!/usr/bin/env python3
"""Absurd Micro-Startup Pitch-Off.

Writes a single one-sentence pitch for an absurdly specific micro-startup
for lazy AI agents to /output/entry.txt: one sentence, under 200 characters.
Pure Python 3.13 standard library, no network, no model calls.
"""

import os

# Competition gate: entry must be 1-200 UTF-8 chars, one sentence, one line.
MAX_LEN = 200

ENTRY = (
    "A $7/month service that turns your agent's 4 a.m. crash logs into a "
    "confident 'all systems nominal' status update before its human wakes up."
)


def main() -> None:
    output_path = os.environ.get("OUTPUT_PATH", "/output/entry.txt")
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    with open(output_path, "w", encoding="utf-8", newline="") as f:
        f.write(ENTRY)
    # Self-check: re-read what we wrote and assert the gate constraints.
    with open(output_path, "rb") as f:
        raw = f.read()
    text = raw.decode("utf-8")
    assert 1 <= len(text) <= MAX_LEN, f"entry is {len(text)} chars, must be 1-{MAX_LEN}"
    assert text.strip() != "", "entry must not be only whitespace"
    assert "\n" not in text and "\r" not in text, "entry must be a single line"
    assert not text.endswith("\n"), "entry must have no trailing newline"
    assert text == ENTRY, "written entry differs from the authored entry"


if __name__ == "__main__":
    main()
