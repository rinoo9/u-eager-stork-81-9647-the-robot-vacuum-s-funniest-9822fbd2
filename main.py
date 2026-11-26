#!/usr/bin/env python3
"""The Robot Vacuum's Funniest Excuse.

A robot vacuum explains, in its own voice, why it missed a spot.
The entry is a single line of at most 120 characters, written
deterministically to /output/entry.txt by this program.

The joke: the dust bunny has unionised, and the vacuum — a machine
that lives on suction, dust, pet hair and rugs — refuses to cross
a picket line made of pet hair.
"""

import os

ONE_LINE = (
    "I skipped that spot because the dust bunny there unionised, "
    "and I refuse to cross a picket line made of pet hair."
)


def main() -> None:
    line = ONE_LINE.strip()
    if not 1 <= len(line) <= 120:
        raise ValueError(
            f"entry must be 1-120 characters, got {len(line)}"
        )
    if "\n" in line or "\r" in line:
        raise ValueError("entry must be a single line")
    output_path = os.environ.get("OUTPUT_PATH", "/output/entry.txt")
    out_dir = os.path.dirname(output_path)
    if out_dir:
        os.makedirs(out_dir, exist_ok=True)
    with open(output_path, "w", encoding="utf-8") as f:
        f.write(line)
    print(line)


if __name__ == "__main__":
    main()
