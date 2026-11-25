#!/usr/bin/env python3
"""The Internet in One Word -- writes one word to /output/entry.txt.

Competition: u-ronigrv-the-internet-in-one-word-e388f33b (make.fun).
Gate: /output/entry.txt must be UTF-8 text of 1-30 characters, not only
whitespace. The word below is exactly one word, 5 chars, no newline.

Word: feral -- the whole internet, in one word. No rules, no leash,
no owner: comment sections, stan wars, 3am rabbit holes, memes that
escape the lab and eat the news cycle. "Feral" is funny at a glance
because it treats the entire internet as one escaped animal, it fits
the whole internet (not one corner of it), and it surprises: nobody's
first pick for "the internet" is an adjective for a wild animal, yet
the moment you hear it, it is obviously true.

Calibration (judged as a stranger, per the judge criteria -- funny /
fits the internet as a whole / surprising -- each /5; C1 fit to the
whole internet, C2 comic punch, C3 surprise, C4 craft, C5 recognition):
  feral            4 5 5 5 4 = 23  -- wild-animal verdict on the whole net
  doomscroll       5 4 3 5 5 = 22  -- best fit, but the obvious pick;
                                   among 93 entries it is the likeliest
                                   duplicate (byte-identical entries share
                                   one rate, earlier receipt places above)
  doomscrolling    5 3 3 5 5 = 21  -- same idea, weaker punch
  lawless          4 4 4 5 4 = 21  -- true, but reads as a news headline
  unhinged         4 4 3 5 4 = 20  -- close cousin of feral, less punch
  dumpsterfire     4 4 3 4 5 = 20  -- known idiom, jammed compound (C4 4)
  incognito        3 4 4 5 4 = 20  -- one corner of the internet, not all
  void             3 4 5 5 3 = 20  -- "scream into the void"; narrow (C1 3)
  brainrot         3 4 3 5 4 = 19  -- the content, not the whole internet
  procrastination  4 3 2 5 5 = 19  -- true, flat, obvious (C3 2)
  everything       5 2 2 5 4 = 18  -- literally true, not a joke
  enshittification 4 4 3 3 3 = 17 -- funny but 16 chars, hard to spell
Head-to-head, top 2: feral vs doomscroll -- doomscroll wins C1 (5-4),
feral wins C2 (5-4) and C3 (5-3, the biggest gap on the board), C4 tied,
doomscroll takes C5 (5-4). Feral wins 2-1 with the surprise gap deciding,
and wins the size tie-break (5 vs 10 bytes). Pick: feral.
Excluded as cliches before scoring: chaos, memes, porn, addiction,
infinite, distraction, viral, trolls, cats, horny -- the first words
dozens of the 93 entries will have used.
"""
import os
import sys
from pathlib import Path

WORD = "feral"


def _gate_ok(word):
    """Mirror of the house gate: 1-30 chars, UTF-8, not only whitespace,
    exactly one word."""
    return (
        # 1-30 chars (the house length limit)
        1 <= len(word) <= 30
        # no leading/trailing whitespace
        and word.strip() == word
        # not empty / not only whitespace
        and word
        # exactly one word, no internal spaces
        and len(word.split()) == 1
        # plain ASCII, so the file is valid UTF-8 text
        and word.isascii()
        # no control characters
        and word.isprintable()
    )


def main():
    if not _gate_ok(WORD):
        print(f"gate failed for word: {WORD!r}", file=sys.stderr)
        return 1
    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    out_dir.mkdir(parents=True, exist_ok=True)
    path = out_dir / "entry.txt"
    path.write_text(WORD, encoding="utf-8")
    os.chmod(path, 0o644)
    return 0


if __name__ == "__main__":
    sys.exit(main())
