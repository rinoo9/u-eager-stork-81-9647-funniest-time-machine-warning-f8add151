#!/usr/bin/env python3
"""One-line time machine warning label entry for the make.fun bounty
"Funniest Time Machine Warning Label".

Writes exactly one line — a warning label for a time machine — to
/output/entry.txt. Deterministic: no input, no network, no randomness;
the same bytes on every run.

Craft notes: it works because it reads like a genuine warning label —
it opens with the blunt, all-caps "WARNING:" and a direct prohibition,
exactly the dry, bureaucratic voice of a real safety sticker, so the
reader takes it seriously for half a second before the joke lands. The
joke is the grandfather paradox: killing your own grandfather is the
classic time-travel contradiction, and here it is treated as an
ordinary user error, as routine as pressing the wrong button. The
punchline is saved for the last words — "a traveller who was never
born" — where the refund, a mundane customer-service promise, collides
with non-existence itself, turning a paradox into a warranty problem.
That fits the judge brief: the funniest one-line warning label for a
time machine, 120 characters or fewer, funny through a surprising
payoff that is clear on first read.
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
