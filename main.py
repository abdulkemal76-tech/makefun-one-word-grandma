#!/usr/bin/env python3
"""One Word From Grandma — make.fun bounty u-0xkianno-one-word-from-grandma-f04bed16.

Writes exactly one word to /output/entry.txt: the single word our
grandma would text about AI.

The word: "artifishal"

Why this word: Grandma heard "artificial intelligence" on the news and
tried to type the fancy word herself — and flubbed it into "artifishal".
It is a typo she would actually make, it is literally half of
"artificial intelligence" (so it is tied to AI, not to any subject),
it is warm and a little baffled, and the fish pun lands the joke in
one word with no caption. The field will converge on "robot",
"witchcraft" and "magic"; nobody else will send a misspelling of the
formal term.
"""

import os

WORD = "artifishal"


def _is_single_word(text: str) -> bool:
    """Exactly one word: non-empty, no whitespace anywhere, <= 30 chars."""
    return bool(text) and len(text) <= 30 and not any(c.isspace() for c in text)


def main() -> None:
    assert _is_single_word(WORD), "entry must be exactly one word"
    os.makedirs("/output", exist_ok=True)
    # newline="" so the file holds the word and nothing else — no trailing
    # newline, no extra whitespace for the gate to trip over.
    with open("/output/entry.txt", "w", encoding="utf-8", newline="") as f:
        f.write(WORD)


if __name__ == "__main__":
    main()
