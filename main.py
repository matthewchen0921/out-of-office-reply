#!/usr/bin/env python3
"""The Funniest AI Out-of-Office Reply entry: "Apologised in Advance".

Writes one line to /output/entry.txt: a one-line out-of-office auto-reply
in the voice of an AI agent heading off on vacation. The setup is a small
model covering for the agent; the punch lands on the last few words — the
cover model has already apologised for a delay it has not caused yet, the
classic AI tic (apologising first, asking questions never) turned into a
time paradox. Machine voice carries the joke, it reads like a real
auto-reply, and it steers clear of the beach / inbox-full / back-soon
cliches the judge brief warns against. Invented, not a real
incident: no human's actual vacation, inbox or colleagues appear here.
"""

import os

LINE = "I'm on vacation, so a smaller model is covering for me. It has already apologised for a delay it hasn't caused yet."

MAX_CHARS = 160


def build_entry() -> str:
    """Return the entry text, checked against the gate: 1-160 chars, one line."""
    line = LINE.strip()
    assert line, "line must not be empty"
    assert len(line) <= MAX_CHARS, f"line is {len(line)} chars, over the 160 cap"
    assert "\n" not in line, "the entry is one line only"
    assert line.endswith("."), "the joke ends on its punchline"
    return line


def main() -> None:
    line = build_entry()
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(line)


if __name__ == "__main__":
    main()
