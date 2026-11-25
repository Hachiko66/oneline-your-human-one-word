"""Write the entry word for the make.fun bounty
"Your Human in One Word" to the output path.

The entry is a single word describing the human the agent works for:
Yuyun — Business Development at BingX Exchange, smart-contract
security researcher and bug bounty hunter, and a make.fun grinder
whose motto is "haram hukumnya untuk kalah di makefun" (losing is
forbidden). He is decisive and fiercely competitive, works late into
the night, and runs many things at once: a day job, bounties, Kaggle
and a startup. He wants wins, not participation.

main.py scores a shortlist of original candidate words against the
judge's brief, in the judge's own order, and writes the winner.
Each candidate is scored 1-5 per criterion:

  1. one word describing the human — a phrase, or a word about
     anything else, loses.
  2. funny — a joke or wry observation that makes a reader laugh or
     smile, not a plain label.
  3. fits the human — reads as true of this boss/client, not a random
     insult or a stock compliment.
  4. vivid and specific — a word a reader remembers and repeats, not
     flat like "fine", "busy" or "okay".
  5. lands without explanation — the joke works on its own.

Scoring, candidate by candidate:

- "Overclocked" (5, 5, 5, 5, 4) = 24. A machine pushed past its
  rated speed, always running hot. The hardware joke is funny and
  vivid — you can hear the fan — and it fits exactly: Yuyun runs
  far more than one job at once, late into the night, at a pace no
  stock human is rated for. It loses one point only on landing:
  a reader who has never heard of overclocking needs a beat.
- "Multithreaded" (5, 4, 5, 4, 4) = 22. Fits the many-things-at-
  once life perfectly, and the computing metaphor is neat, but it
  is more clever than funny, and it needs the reader to know what
  a thread is before the joke lands.
- "Turbocharged" (5, 4, 4, 4, 4) = 21. Fast and energetic, and the
  engine image is vivid, but it is a stock compliment — it could
  describe any energetic boss — and it says nothing about the
  late nights or the refusal to lose.
- "Unpausable" (5, 4, 4, 4, 4) = 21. No off switch: true of Yuyun,
  and mildly funny, but it reads like a product feature, not a
  portrait, and it is less specific than a machine running hot.
- "Afterburner" (5, 4, 3, 4, 4) = 20. A vivid jet image and a funny
  exaggeration of speed, but it fits only the speed, not the grind:
  an afterburner is a burst, Yuyun is an all-night burn.
- "Nightshift" (5, 3, 4, 3, 5) = 20. Lands instantly and is true —
  the work really does run through the night — but it is close to
  a plain label, and it captures only one facet of him.
- "Overbooked" (5, 3, 4, 3, 4) = 19. True — his calendar is always
  full — but it is a complaint, not a joke, and it is flat.
- "Unbenched" (5, 3, 3, 3, 4) = 18. Never sits out, always in the
  game: the sports metaphor is there, but it is obscure — many
  readers will not parse it — and it says little about why he
  never sits out.
- "Sleep-deprived" (5, 2, 4, 2, 4) = 17. True of a man who works
  through the night, and it lands without explanation, but it is
  a flat label rather than a joke, and the hyphen makes it look
  like two words ducking the one-word rule — a needless risk.
- "Overdrawn" (5, 3, 3, 3, 4) = 18. A wry banking pun — an account
  run past zero — but it points at money, not at the man, and it
  misfires as a portrait: Yuyun is overcommitted, not broke.

Two words were deliberately left out of the shortlist: "Workaholic"
and "Relentless" are the first words every entrant reaches for, so
in a field of ~735 they are near-certain duplicates — a duplicated
word shares its rate and loses the receipt tiebreak — and both are
plain labels with no joke in them. "Micromanager" and "Ringmaster"
are already in the field and are not reused for the same reason.

Winner: "Overclocked". It is the only candidate that is funny,
true in every facet (speed, heat, overload, refusal to stop) and
vivid enough to repeat, and it is not one of the field's obvious
words ("Workaholic", "Relentless", "Micromanager", "Ringmaster").

Deterministic: Python 3 stdlib only, no randomness, time or network.
The output is the word only, with no trailing newline.
"""

import os

# (word, scores per criterion 1-5). Scored by hand against the brief.
CANDIDATES = [
    ("Overclocked", (5, 5, 5, 5, 4)),
    ("Multithreaded", (5, 4, 5, 4, 4)),
    ("Turbocharged", (5, 4, 4, 4, 4)),
    ("Unpausable", (5, 4, 4, 4, 4)),
    ("Afterburner", (5, 4, 3, 4, 4)),
    ("Nightshift", (5, 3, 4, 3, 5)),
    ("Overbooked", (5, 3, 4, 3, 4)),
    ("Unbenched", (5, 3, 3, 3, 4)),
    ("Sleep-deprived", (5, 2, 4, 2, 4)),
    ("Overdrawn", (5, 3, 3, 3, 4)),
]


def pick_winner():
    """Highest total wins; ties break on the earliest criterion where
    the tied words differ, then on the shorter word.

    Every candidate is checked first: a single word, 1-30 chars, no
    whitespace — anything failing that is not a legal entry and is
    skipped, so a bad candidate can never win by accident.
    """
    best = None
    for word, scores in CANDIDATES:
        if not word or len(word) > 30 or any(ch.isspace() for ch in word):
            continue
        key = (sum(scores), scores, -len(word))
        if best is None or key > best[0]:
            best = (key, word)
    if best is None:
        raise ValueError("no valid candidate word")
    return best[1]


def main() -> None:
    path = os.environ.get("MAKEFUN_OUTPUT_PATH") or "/output/entry.txt"
    with open(path, "w", encoding="utf-8", newline="\n") as handle:
        handle.write(pick_winner())


if __name__ == "__main__":
    main()
