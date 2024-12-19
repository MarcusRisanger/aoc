"""
AOC 2020, Day 1
"""

import re


def clean_input(input: str) -> list[str]:
    return input.split("\n\n")


def part1(input: list[str]) -> str:
    """Counts all lines where all elements in `need` are found."""
    need = {"byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"}
    return str(sum(1 if all([i in line for i in need]) else 0 for line in input))


def part2(input: list[str]) -> str:
    """Counts all lines where all the different required patterns are found and valid."""
    patterns = [
        r"byr:(19[2-9]\d|200[0-2])",
        r"iyr:(20(?:[1]\d|20))",
        r"eyr:(20(?:2\d|30))",
        r"hgt:(1(?:[5-8]\d|9[0-3])cm|(?:59|6\d|7[0-6])in)",
        r"hcl:\#[0-9a-f]{6}",
        r"ecl:(amb|blu|brn|gry|grn|hzl|oth)",
        r"pid:[0-9]{9}(?!\d)",
    ]
    return str(
        sum(1 if all([re.findall(p, line) for p in patterns]) else 0 for line in input)
    )


if __name__ == "__main__":
    from aocd.models import Puzzle

    # Get puzzle details and set up input
    puzzle = Puzzle(year=2020, day=4)
    input_data = clean_input(puzzle.input_data)

    # Submit answers
    puzzle.answer_a = part1(input_data)
    puzzle.answer_b = part2(input_data)
