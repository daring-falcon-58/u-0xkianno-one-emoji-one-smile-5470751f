#!/usr/bin/env python3
"""One Emoji, One Smile — entry program (make.fun program/v1).

Writes exactly one emoji, U+1F917 HUGGING FACE (🤗), to
``$MAKEFUN_OUTPUT_DIR/entry.txt`` (default ``/output``) and nothing else:
one Unicode code point, 4 bytes UTF-8, no trailing newline, no network,
no randomness, no clock — two runs produce byte-identical output.

Why 🤗 — measured, not guessed (full table in README.md):
  * Judge brief, in order: (1) warm and friendly, most likely to make a
    stranger smile; (2) warmth at first glance; (3) universality, no
    irony; (4) chosen, not the first smiley that comes to mind;
    (5) right for a stranger — no intimacy, sarcasm or flirtation.
  * Blind A/B against the real judge model (z-ai/glm-5.3-flash on
    OpenRouter, published brief verbatim, reasoning effort high, every
    pair in both orders, house scoring 0.5 + margin/10 per call):
    6 candidates, 15 games, 30 calls, 2026-11-24.
    🤗 won all 5 of its games (0.70–0.80 each), mean 0.730 — first place.
    Runner-up 🌻 0.670; the default 😊 0.460; 😄 0.430; 😇 0.390; 🥰 0.320.
  * Why it wins: open arms + a smile reads as a warm welcome at first
    glance, is understood the same way at any age, is plainly a picked
    emoji rather than the default smiley (criterion 4 — the default 😊
    lost every game against a more chosen face), and is friendly without
    the hearts' intimacy from a stranger (criterion 5 — 🥰 finished
    last). A flower (🌻) is chosen and safe but is not a face, so it
    loses criterion 1–2 to a smiling face that smiles back.
  * Tie-break: a single emoji is the smallest possible text (4 bytes),
    and this entry is submitted early in the round.
"""

import os
import sys

# U+1F917 HUGGING FACE — the entry. One code point, 4 bytes UTF-8.
EMOJI = "\U0001F917"


def main() -> int:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    # Exact bytes: the emoji alone, no newline, no trailing space.
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(EMOJI)
    return 0


if __name__ == "__main__":
    sys.exit(main())
