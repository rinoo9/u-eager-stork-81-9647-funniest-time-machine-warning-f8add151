#!/usr/bin/env python3
"""One-line time machine warning label entry for the make.fun bounty
"Funniest Time Machine Warning Label".

Writes exactly one line — a warning label for a time machine — to
/output/entry.txt. Deterministic: no input, no network, no randomness;
the same bytes on every run.
"""

import os

LABEL = (
    "WARNING: Do not kill your grandfather. The machine cannot refund "
    "a traveller who was never born."
)


def main() -> None:
    assert 1 <= len(LABEL) <= 120, f"label is {len(LABEL)} characters"
    assert "\n" not in LABEL and LABEL == LABEL.strip()
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="") as f:
        f.write(LABEL)


if __name__ == "__main__":
    main()
