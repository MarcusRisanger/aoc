"""
AOC 2020, Day 3
"""

import math


def clean_input(input: str) -> list[str]:
    return input.splitlines()


def traverse(input: list[str], slope: int = 3, speed: int = 1) -> int:
    trees = 0
    index = 0
    for i in range(0, len(input), speed):
        if input[i][index] == "#":
            trees += 1

        # When reaching right side of slope, start over from left side
        index = (index + slope) % len(input[0])
    return trees


def part1(input: list[str]) -> str:
    return str(traverse(input))


def part2(input: list[str]) -> str:
    return str(
        math.prod([*map(traverse, [input] * 5, [1, 3, 5, 7, 1], [1, 1, 1, 1, 2])])
    )


if __name__ == "__main__":
    from aocd.models import Puzzle

    # Get puzzle details and set up input
    puzzle = Puzzle(year=2020, day=3)
    input_data = clean_input(puzzle.input_data)

    # Submit answers
    puzzle.answer_a = part1(input_data)
    puzzle.answer_b = part2(input_data)
