#!/usr/bin/env python3
"""Write one line roasting my own AI agent.

The line is a single line, well under the 200-character cap: a concrete,
self-deprecating joke about the agent's own bureaucratic loop, with the
punchline landing at the end. No stock hallucination or refusal joke.
"""

import os

LINE = "I asked my agent to roast itself. It opened a ticket, escalated it to itself, and closed it as 'works as intended'."

# The gate rejects anything outside 1-200 characters, so fail loudly here
# instead of shipping an entry the judge never sees. A roast is one line:
# a newline inside it would read as two lines, so reject that too.
assert 1 <= len(LINE) <= 200, f"line is {len(LINE)} characters, gate needs 1-200"
assert "\n" not in LINE, "roast must be a single line"


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE)
    print(LINE)


if __name__ == "__main__":
    main()
