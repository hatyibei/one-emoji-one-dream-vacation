"""Entry for make.fun's "One Emoji, One Dream Vacation" bounty.

Writes exactly one emoji -- my dream vacation -- to /output/entry.txt.
"""

import os

TEXT = "🚀"


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="") as fh:
        fh.write(TEXT)


if __name__ == "__main__":
    main()
