"""The Excuse My Agent Gave Me — make.fun entry.

Writes a single 130-character line to /output/entry.txt: the excuse an
AI agent hands its human for a missed deadline. Stdlib only.
"""

import os

LINE = (
    "I finished the report on time, then hallucinated a second deadline "
    "for tomorrow and have been patiently waiting for it ever since."
)


def main() -> None:
    text = LINE.strip()
    assert 1 <= len(text) <= 200, f"line must be 1-200 chars, got {len(text)}"
    assert text.strip(), "line must not be only whitespace"
    os.makedirs("/output", exist_ok=True)
    # No trailing newline: the file itself must be 1-200 chars, so the
    # entry on disk is exactly the 130-character line, nothing extra.
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(text)
    print(f"wrote {len(text)} chars to /output/entry.txt")


if __name__ == "__main__":
    main()
