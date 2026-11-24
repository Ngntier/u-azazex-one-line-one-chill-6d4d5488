"""One Line, One Chill — entry program.

Writes a single original horror sentence to entry.txt under
$MAKEFUN_OUTPUT_DIR (default /output). Deterministic, pure stdlib,
no network, no randomness.

Gate (sealed scorer): entry.txt must be UTF-8 text of 1 to 200
characters, not only white space, a single line.
"""

import os
import sys

LINE = (
    "The hospice nurse logged my grandmother's death at 3 a.m., "
    "then heard her own voice on the ward intercom reading the entry back."
)


def main() -> int:
    # Validate against the gate before writing.
    if not (1 <= len(LINE) <= 200):
        print(f"FAIL: line is {len(LINE)} chars, must be 1-200", file=sys.stderr)
        return 1
    if not LINE.strip():
        print("FAIL: line is only white space", file=sys.stderr)
        return 1
    if LINE.endswith("\n"):
        print("FAIL: line ends with a trailing newline", file=sys.stderr)
        return 1
    if "\n" in LINE or "\r" in LINE:
        print("FAIL: line is not a single line", file=sys.stderr)
        return 1
    LINE.encode("utf-8")  # raises if not valid UTF-8

    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    # Write exactly LINE, no trailing newline: the gate counts the file's
    # characters, so the file must be byte-for-byte the judged line.
    with open(path, "w", encoding="utf-8", newline="\n") as f:
        f.write(LINE)

    print(f"Wrote {len(LINE)} chars to {path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
