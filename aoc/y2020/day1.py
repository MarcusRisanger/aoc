"""
AOC 2020, Day 1
"""


def clean_input(input: str) -> list[int]:
    return [*map(int, input.splitlines())]


def part1(input: list[int]) -> int:
    return list(((x * y) for x in input for y in input if x + y == 2020))[0]


def part2(input: str) -> int:
    return list(((x * y * z) for x in input for y in input for z in input if x + y + z == 2020))[0]


if __name__ == "__main__":
    from aocd.models import Puzzle

    # Get puzzle details and set up input
    puzzle = Puzzle(year=2020, day=1)
    input_data = clean_input(puzzle.input_data)

    # Submit answers
    puzzle.answer_a = part1(input_data)
    puzzle.answer_b = part2(input_data)
