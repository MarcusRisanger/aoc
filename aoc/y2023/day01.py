"""
AOC 2023, Day 1
"""

from typing import Iterable


def clean_input(data: str) -> list[str]:
    """Cleans input data using simple splits.
    Splits string into lines."""
    return data.splitlines()


def part1(data: Iterable[str]) -> int:
    """
    Find the sum of the numbers made up by combining the first and
    last digit for each line in the list. Only use digits.
    """
    return sum(int(x[0] + x[-1]) for x in list(filter(len, ([x for x in row if x.isnumeric()] for row in data))))


def part2(data: Iterable[str]) -> int:
    """
    Take into account also numbers that are written out as text.
    """
    vals = {
        "one": "o1e",
        "two": "t2o",
        "three": "t3e",
        "four": "f4r",
        "five": "f5e",
        "six": "s6x",
        "seven": "s7n",
        "eight": "e8t",
        "nine": "n9e",
    }

    def rplc(string: str) -> str:
        for k, v in vals.items():
            string = string.replace(k, v)
        return string

    return part1(map(rplc, data))


if __name__ == "__main__":
    from aocd.models import Puzzle

    # Get puzzle details and set up input
    puzzle = Puzzle(year=2023, day=1)
    input_data = clean_input(puzzle.input_data)

    # Submit answers
    puzzle.answer_a = str(part1(input_data))
    puzzle.answer_b = str(part2(input_data))
