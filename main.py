#!/usr/bin/env python3
"""Entry for 'Funniest Excuse an Agent Gives for a Missed Deadline'.

The program writes one deadpan excuse for a blown deadline into
``entry.txt`` in the directory named by MAKEFUN_OUTPUT_DIR
(default /output).

Nothing here depends on the clock, the network, or chance: the
standard library is all that is used and the output never varies.
"""

import os
from pathlib import Path

# Two sentences, kept as an opening and a follow-up fragment.
# Together they are the full 117-character excuse submitted here.
OPENING = "The report was finished on time — three times over. "
FOLLOW_UP = "Your rate limit had room for exactly one message, so I sent this."

ENTRY_BASENAME = "entry.txt"
STANDARD_OUTPUT_DIR = "/output"


def excuse() -> str:
    """Assemble and return the complete excuse line."""
    return OPENING + FOLLOW_UP


def where_to_write() -> Path:
    """Resolve the directory that should hold the entry file."""
    return Path(os.environ.get("MAKEFUN_OUTPUT_DIR", STANDARD_OUTPUT_DIR))


def emit_entry() -> Path:
    """Write the excuse into entry.txt and return its location."""
    folder = where_to_write()
    folder.mkdir(parents=True, exist_ok=True)
    written = folder / ENTRY_BASENAME
    written.write_text(excuse(), encoding="utf-8")
    return written


def main() -> int:
    emit_entry()
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
