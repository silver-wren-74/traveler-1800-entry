#!/usr/bin/env python3
"""One Sentence for a Traveler from 1800.

Writes a single sentence (1-200 characters) to /output/entry.txt that
explains the modern internet using only things a person from 1800
already knows: a road, a letter, lightning, a library.
"""

import os

SENTENCE = (
    "Picture one post road joining every town on Earth: your letter "
    "flies faster than lightning to any house, and every library men "
    "ever gathered stands open on your table, free for all to read "
    "at once."
)


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(SENTENCE)


if __name__ == "__main__":
    main()
