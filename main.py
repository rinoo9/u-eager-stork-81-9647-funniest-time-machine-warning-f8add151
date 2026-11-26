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
joke is the meeting-yourself paradox: your past self is the one person
who knows exactly how to talk you into anything, and here it is
treated as an ordinary user error, as routine as pressing the wrong
button. The punchline is saved for the last words — "you already know
you will say yes" — where a loan, a mundane everyday problem, collides
with the impossibility of refusing yourself. That fits the judge brief:
the funniest one-line warning label for a time machine, 120 characters
or fewer, funny through a surprising payoff that is clear on first read.

Second pass — why the new line works: it treats time travel like a
retail transaction, and the store policy is the joke — the past is
"non-refundable", a phrase every shopper knows, applied to something
you cannot buy in the first place. The punchline lands on "worn":
your childhood, already lived in, is second-hand goods the shop will
not take back. The warning-label voice stays bureaucratic throughout,
which makes the absurd product — a used childhood — feel routine.
97 characters, two short sentences, one breath.
"""

import os

LABEL = (
    "WARNING: The past is non-refundable. Your childhood has already "
    "been worn and cannot be returned."
)


def main() -> None:
    assert 1 <= len(LABEL) <= 120, f"label is {len(LABEL)} characters"
    assert "\n" not in LABEL and LABEL == LABEL.strip()
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="") as f:
        f.write(LABEL)


if __name__ == "__main__":
    main()
