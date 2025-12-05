import re


Range = tuple[int, int]
Ingredients = list[int]


def clean_data(inp: str) -> tuple[list[Range], Ingredients]:
    r, i = inp.split("\n\n")
    ranges = [(int(a), int(b)) for a, b in re.findall(r"(\d+)\-(\d+)", r)]
    ints = [int(n) for n in i.splitlines()]
    return ranges, ints


def part1(ranges: list[Range], ingredients: Ingredients) -> int:
    return sum(1 for i in ingredients if any(i in range(r[0], r[1] + 1) for r in ranges))


def part2(ranges: list[Range]) -> int:
    ranges = sorted(ranges, key=lambda x: x[0])
    ids, current = 0, 0  # Starting point
    for start, end in sorted(ranges):
        start = max(current + 1, start)  # Avoid overlap with next interval
        ids += max(0, end - start + 1)
        current = max(current, end)
    return ids


if __name__ == "__main__":
    from aocd.models import Puzzle

    # Get puzzle details and set up input
    puzzle = Puzzle(year=2025, day=5)
    ranges, ingredients = clean_data(puzzle.input_data)

    # Submit answers
    puzzle.answer_a = str(part1(ranges, ingredients))
    puzzle.answer_b = str(part2(ranges))
