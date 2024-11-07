"""
AOC 2023, Day 2
"""
import math
import re

from typing import Iterable
from collections import defaultdict


def clean_input(data: str) -> list[str]:
    """No reason to clean input today."""
    return data.splitlines()


def part1(data: Iterable[str]) -> int:
    """
    Using a fixed bag and regexing the values and colors
    from each line - each line corresponds to one game.

    Summing the
    """
    bag = {"red": 12, "green": 13, "blue": 14}

    def row(line: str) -> bool:
        for value, color in re.findall(r"(\d+) (\w+)", line):
            if bag[color] < int(value):
                return False
        return True

    return sum(i + 1 for i, line in enumerate(data) if row(line))


def part2(data: Iterable[str]) -> int:
    """
    Using defaultdict as bag to simplify the comparison between
    non-existing dict key and regexed values.
    """

    def row(line: str) -> int:
        bag: dict[str, int] = defaultdict(int)
        for value, color in re.findall(r"(\d+) (\w+)", line):
            bag[color] = max(bag[color], int(value))
        return math.prod(bag.values())

    return sum(map(row, data))


if __name__ == "__main__":
    from aocd.models import Puzzle

    # Get puzzle details and set up input
    puzzle = Puzzle(year=2023, day=2)
    input_data = clean_input(puzzle.input_data)

    # Submit answers
    puzzle.answer_a = part1(input_data)
    puzzle.answer_b = part2(input_data)
