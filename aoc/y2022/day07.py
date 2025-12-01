"""
AOC 2022, day 7:
   - Cleaning input with match-case type solution instead of previous "regular" flow.
   - Big improvement with using `itertools.accumulate` to handle directory names.
   - Parts 1 and 2 are easy to produce on correctly parsed input.
"""

from collections import defaultdict
from itertools import accumulate


def clean_input(input_data: str) -> dict[str, int]:
    """Returns dict of directory keys and size values."""
    # Let's get rid of the entirely useless rows immediately
    movements = input_data.replace("$ ls\n", "").splitlines()
    dirs = defaultdict(int)
    # Loop over our tree movements
    for row in movements:
        match row.split():
            case "$", "cd", "/":
                # Moving into root - establish directory tree
                current_dir = ["/"]
            case "$", "cd", "..":
                # Moving out of a directory - remove last element
                current_dir.pop()
            case "$", "cd", dir:
                # Navigating into a directory - append to list
                current_dir.append(dir + "/")
            case "dir", _:
                # To not screw up the next case.. :D
                pass
            case size, _:
                # Increment directory size for all directoryies
                # where the current directory resides
                for dir in accumulate(current_dir):
                    dirs[dir] += int(size)
    return dirs


def part1(input_data: dict[str, int]) -> int:
    """Returns size dirs with a size of at most 100000"""
    return sum(v for v in input_data.values() if v <= 100_000)


def part2(input_data: dict[str, int]) -> int:
    """Returns size of smallest dir that can be deleted to free up enough space"""
    return min(v for v in input_data.values() if v >= (-40_000_000 + input_data["/"]))


if __name__ == "__main__":
    from aocd.models import Puzzle

    # Get puzzle details and set up input
    puzzle = Puzzle(year=2022, day=7)
    input_data = clean_input(puzzle.input_data)

    # Submit answers
    puzzle.answer_a = part1(input_data)
    puzzle.answer_b = part2(input_data)
