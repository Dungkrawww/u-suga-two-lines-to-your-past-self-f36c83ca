#!/usr/bin/env python3
"""u-suga-two-lines-to-your-past-self-f36c83ca: Two Lines to Your Past Self.

Writes the two-line entry to /output/entry.txt for make.fun's
program/v1 judge: line 1 warns my past self about one specific
moment; line 2 says why it mattered and what changed. Gate: UTF-8
text, 1-280 characters.
Local check 2026-11-25: 2 runs byte-identical, output 189 chars.
"""

import os

ENTRY = (
    "Don't skip the backup before the update \u2014 the one time you do, the laptop dies mid-install.\n"
    "I lost a weekend rebuilding everything, so now the backup runs before I even read the changelog.\n"
)


def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
