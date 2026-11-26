#!/usr/bin/env python3
"""The Dog Reviews the Mailman.

Writes one funny one-line review a dog gives the mailman to
/output/entry.txt. Standard library only, fully deterministic:
the same line is written on every run.
"""

import os

OUTPUT_PATH = "/output/entry.txt"

# The review: the mailman tried a bribe, the dog took it and barked
# anyway. Five stars for the biscuit, one star for the mailman.
LINE = (
    "He tried to bribe me with a biscuit. "
    "I ate it, then barked anyway. "
    "Five stars for the biscuit, one star for the mailman."
)


def write_entry(path: str = OUTPUT_PATH) -> str:
    """Write the review as a single line and return it."""
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w", encoding="utf-8") as f:
        f.write(LINE + "\n")
    return LINE


def main() -> None:
    line = write_entry()
    print(f"Wrote {len(line)} characters to {OUTPUT_PATH}")


if __name__ == "__main__":
    main()
