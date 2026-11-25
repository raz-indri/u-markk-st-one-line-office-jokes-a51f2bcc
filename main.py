"""One-Line Office Jokes entry for make.fun.

Writes a single one-line office joke to /output/entry.txt.
The joke turns on a real office detail (the reply-all thread)
and lands its laugh in the last few words.
"""

import os

JOKE = (
    "Someone replied-all to 214 people to say 'please remove me "
    "from this thread,' and 38 people replied-all to agree."
)


def main():
    # The gate requires 1-199 characters of UTF-8 text, one line.
    assert 1 <= len(JOKE) <= 199, "joke must be 1-199 characters"
    assert "\n" not in JOKE, "joke must be a single line"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(JOKE)


if __name__ == "__main__":
    main()
