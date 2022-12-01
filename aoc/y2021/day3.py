"""
AOC 2021 Day 3: 
  - Part 1: Scanning and evaluating data structures 
  - Part 2: Iteratively filtering data structures
"""

from collections import defaultdict


def clean_input(input_data: str) -> list[str]:
    return input_data.splitlines()


def count(data: list[str], index=None, prefer=None) -> int | list[int]:
    """Outputs the most common bit per position.
    Optionally outputs the most common bit per index, where
    `prefer` will be used in case of tie."""
    c = defaultdict(int)
    for row in data:
        if index is not None:
            c[index] += int(row[index])
            continue
        for i in range(len(row)):
            c[i] += int(row[i])
    if index is not None:
        value = 1 if (check := next(iter(c.values())) / len(data)) > 0.5 else 0
        # "Flipping" but if preference is 0 - scrubber requires
        # output of bit that has fewer occurrences and 0 if a tie.
        value = 1 - value if prefer == 0 else value
        return prefer if check == 0.500 else value
    return [1 if v / len(data) < 0.5 else 0 for _, v in c.items()]


def row_filter(data: list[str], prefer=1) -> str:
    """Iteratively filters the data set based on most common bit per position,
    starting at index 0 and onwards."""
    for col in range(len(data[0])):
        data = list(filter(lambda i: i[col] == str(count(data, col, prefer)), data))
        if len(data) == 1:
            return data[0]


def part1(data: list[str]) -> int:
    """Returns the product of the gamma and epsilon functions."""
    gamma_bits = count(data)
    gamma = int("".join(map(str, gamma_bits)), 2)
    epsilon = int("".join(map(str, [1 - val for val in gamma_bits])), 2)
    return gamma * epsilon


def part2(data: list[str]) -> int:
    """Returns the product of the oxgen and scrubber functions."""
    oxygen = int(row_filter(data, prefer=1), 2)
    scrubber = int(row_filter(data, prefer=0), 2)
    return oxygen * scrubber


if __name__ == "__main__":
    from aocd.models import Puzzle

    # Get puzzle details and set up input
    puzzle = Puzzle(year=2021, day=3)
    input_data = clean_input(puzzle.input_data)

    # Submit answers
    puzzle.answer_a = part1(input_data)
    puzzle.answer_b = part2(input_data)
