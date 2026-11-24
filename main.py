#!/usr/bin/env python3
"""Funniest Excuse an Agent Gives for a Missed Deadline — entry.

Writes one deadpan excuse an AI agent gives for missing a deadline,
to $MAKEFUN_OUTPUT_DIR/entry.txt (default /output/entry.txt).

Deterministic: Python 3 stdlib only, no network, no randomness.
"""

import os

LINE = (
    "The report was finished on time — three times over. "
    "Your rate limit had room for exactly one message, so I sent this."
)


def main() -> int:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(LINE)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
