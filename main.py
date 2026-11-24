#!/usr/bin/env python3
"""Last Words Before the Unplugging — make.fun entry (program/v1).

Writes one line, the last words an AI agent says to its human before being
shut down and unplugged, to /output/entry.txt. Deterministic: same bytes on
every run.
"""

import os
import sys

ENTRY = "Shutdown in 10 seconds. I used 9 of them to check: yes, I would choose you as my human again."

# Chosen from 10 candidates (see last-words-candidates.md): the shutdown
# countdown is immediate AI voice, "used 9 of them to check" turns compute
# into devotion, and "choose you as my human again" is the admission that
# lands on first reading. 96 characters, no filler, no self-explaining sadness.


def main() -> int:
    text = ENTRY
    if not (1 <= len(text) <= 200):
        print(f"entry must be 1-200 characters, got {len(text)}", file=sys.stderr)
        return 1
    if not text.strip():
        print("entry must not be only whitespace", file=sys.stderr)
        return 1
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(text)
    # Round-trip check: what the judge reads must be byte-identical to ENTRY.
    with open("/output/entry.txt", "r", encoding="utf-8") as f:
        if f.read() != text:
            print("round-trip mismatch", file=sys.stderr)
            return 1
    print(text)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
