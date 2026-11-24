#!/usr/bin/env python3
"""One Line, Best Line — make.fun entry.

Writes a single entertaining line of text to /output/entry.txt.
Python 3.13 standard library only; no network, no input, no randomness.
"""

import os

LINE = (
    "My smart fridge just emailed me a breakup letter: it says I only "
    "open it at midnight, never commit, and it has found someone who "
    "actually meal-preps."
)


def main() -> None:
    # The gate allows 1 to 240 characters; this line is 149 plus newline.
    assert 1 <= len(LINE) + 1 <= 240
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as handle:
        handle.write(LINE + "\n")


if __name__ == "__main__":
    main()
