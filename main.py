"""The Funniest Sick-Day Excuse — entry program.

Writes a single-line sick-day excuse to $MAKEFUN_OUTPUT_DIR/entry.txt
and self-checks the competition gate: UTF-8 text, 1-200 characters,
not whitespace-only.
"""

import os
import sys

ENTRY = "Sorry, can't come in \u2014 my bed has filed for custody of me and the judge ruled in its favour."

MIN_CHARS = 1
MAX_CHARS = 200


def main() -> int:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR")
    if not out_dir:
        print("MAKEFUN_OUTPUT_DIR is not set", file=sys.stderr)
        return 1

    text = ENTRY
    if not (MIN_CHARS <= len(text) <= MAX_CHARS):
        print(f"gate failed: {len(text)} chars, need {MIN_CHARS}-{MAX_CHARS}",
              file=sys.stderr)
        return 1
    if not text.strip():
        print("gate failed: entry is whitespace-only", file=sys.stderr)
        return 1

    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(text)

    # Read-back verification: the file on disk must be exactly the entry.
    with open(path, "r", encoding="utf-8") as f:
        written = f.read()
    if written != text:
        print("gate failed: read-back mismatch", file=sys.stderr)
        return 1
    if "\n" in written:
        print("gate failed: entry must be a single line", file=sys.stderr)
        return 1

    print(f"wrote {path} ({len(text)} chars)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
