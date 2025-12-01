from collections import defaultdict

Page = str
Rules = dict[Page, set[Page]]
Manual = list[Page]


def clean_input(inp: str) -> tuple[list[Manual], Rules]:
    """
    Parse raw input into a list of manuals and associated sorting rules.

    Rules are given as a dictionary with Page keys and the allowed
    succeeding pages in a set as values.
    """
    rules, manuals = inp.split("\n\n")

    m = [m.split(",") for m in manuals.splitlines()]

    r = defaultdict(set)
    for rule in rules.splitlines():
        before, after = rule.split("|")
        r[before].add(after)

    return m, r


def is_valid(manual: Manual, rules: Rules) -> bool:
    """
    List is valid if all succeeding elements can be found in the "valid after" set
    for each index in the manual.
    """
    return all(all(m in rules[val] for m in manual[i + 1 :]) for i, val in enumerate(manual))


def parse_manual(manual: Manual, rules: Rules) -> int:
    """Returns middle page value of valid manual."""
    return int(manual[len(manual) // 2]) if is_valid(manual, rules) else 0


def part1(manuals: list[Manual], rules: Rules) -> int:
    """Sum up middle numbers in all valid manuals."""
    return sum(parse_manual(m, rules) for m in manuals)


def page_sort(manual: Manual, rules: Rules) -> Manual:
    """Get a correctly sorted Manual."""

    def get_next(manual: Manual) -> Page:  # type: ignore[return]
        """Get next page, remove page from passed Manual."""
        for i, page in enumerate(manual):
            other = [m for m in manual if m != page]
            if all(o in rules[page] for o in other):
                manual.pop(i)
                return page

    manual = manual.copy()
    out = []
    while manual:
        out.append(get_next(manual))
    return out


def part2(manuals: list[Manual], rules: Rules) -> int:
    """Get invalid manuals"""
    return sum(parse_manual(page_sort(m, rules), rules) for m in manuals if not is_valid(m, rules))


if __name__ == "__main__":
    from aocd.models import Puzzle

    # Get puzzle details and set up input
    puzzle = Puzzle(year=2024, day=5)
    input_data = clean_input(puzzle.input_data)
    # Submit answers
    puzzle.answer_a = str(part1(*input_data))
    puzzle.answer_b = str(part2(*input_data))
