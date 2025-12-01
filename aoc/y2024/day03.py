import re
from math import prod


def part1(inp: str) -> int:
    """
    Regex finds comma separated pairs of 1-3 length digits
    within regular parens after an instance of `mul`.
    """
    return sum(prod(map(int, pair)) for pair in re.findall(r"mul\((\d{1,3}),(\d{1,3})\)", inp))


def part2(inp: str) -> int:
    """
    Regex finds all substrings between `do()` (or start of line)
    and `don't()` (and end of line). Must be run with single-line flag
    """
    return sum(map(part1, re.findall(r"(?:do\(\)|^)(.*?)(?:don\'t\(\)|$)", inp, flags=re.S)))


if __name__ == "__main__":
    from aocd.models import Puzzle

    # Get puzzle details and set up input
    puzzle = Puzzle(year=2024, day=3)

    # Submit answers
    puzzle.answer_a = str(part1(puzzle.input_data))
    puzzle.answer_b = str(part2(puzzle.input_data))
