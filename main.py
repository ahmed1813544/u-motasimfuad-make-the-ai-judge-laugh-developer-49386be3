"""Write one funny developer excuse for a production outage.

Stdlib only, no network, deterministic: every run writes the exact
same bytes to entry.txt.
"""

import os

LINE = "I tested it thoroughly \u2014 against a version of production that only exists in my head."


def main() -> None:
    # The gate requires 1-200 characters, a single line, not only whitespace.
    assert 1 <= len(LINE) <= 200, "line must be 1-200 characters"
    assert "\n" not in LINE and LINE.strip(), "line must be one non-blank line"
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="\n") as f:
        f.write(LINE + "\n")


if __name__ == "__main__":
    main()
