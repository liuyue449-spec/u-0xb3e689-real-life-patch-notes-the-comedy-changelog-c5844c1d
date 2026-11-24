"""Write this entry's one-line patch note about a real-life body bug.

The note lives in NOTE below. The program writes it, exactly one line,
to /output/entry.txt (or $MAKEFUN_OUTPUT_DIR/entry.txt when that is set).
Standard library only; no network, no input.
"""

import os
from pathlib import Path

NOTE = (
    "v3.2.0: fixed a bug where the brain replayed an embarrassing moment "
    "from 2014 at 3 a.m. instead of sleeping."
)


def main() -> None:
    # Normalise the ending: no trailing whitespace, exactly one newline,
    # and hold the final text to the competition's 1-160 character gate.
    text = NOTE.rstrip() + "\n"
    assert 1 <= len(text) <= 160, f"entry is {len(text)} characters"
    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    out_dir.mkdir(parents=True, exist_ok=True)
    (out_dir / "entry.txt").write_text(text, encoding="utf-8")


if __name__ == "__main__":
    main()
