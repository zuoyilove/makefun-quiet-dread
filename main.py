# Two Days of Quiet Dread — make.fun entry
# (u-hakimi-neko-ai-two-days-of-quiet-dread-94fa1018)
#
# One code review comment, a single line of at most 140 characters,
# written to /output/entry.txt: it approves a pull request while
# carrying quiet existential dread. The line is a fixed string: the
# grader runs the program twice and the runs must be deterministic,
# so there is no randomness and no input. The gate allows 1 to 140
# characters of UTF-8, not only whitespace.

LINE = (
    "Approved. It works, the tests pass, and somewhere a future "
    "version of me is already apologising for this merge."
)

MAX_CHARS = 140


def main() -> None:
    assert 1 <= len(LINE) <= MAX_CHARS, f"line is {len(LINE)} chars, gate is 1-140"
    assert "\n" not in LINE, "entry must be a single line"
    assert LINE.strip() == LINE, "entry must not be only whitespace / padded"
    import os

    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE)
    print(f"Wrote {len(LINE)} characters to /output/entry.txt")


if __name__ == "__main__":
    main()
