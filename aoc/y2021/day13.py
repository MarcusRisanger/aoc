"""
AOC 2021, Day 13:
  - Folding paper!
  - Practice with numpy arrays
"""

import numpy as np
import re


def clean_input(input_data: str) -> tuple[np.ndarray, list[tuple[str, int]]]:
    """Parses x, y pairs into a boolean array.
    Parses instructions to a list."""
    dots, folds = input_data.split("\n\n")

    array = np.zeros((2000, 2000), int)
    for row in dots.splitlines():
        x, y = row.split(",")
        array[int(y), int(x)] = 1

    instructions = []
    for row in folds.splitlines():
        for axis, slice in re.findall(r"(\w)=(\d+)", row):
            instructions.append((axis, int(slice)))

    return array, instructions


def fold_origami(array: np.ndarray, instructions: list[tuple[str, int]]) -> int:
    count = None
    for axis, slice in instructions:
        if axis == "x":
            # Takes array until slice column (first arg: row slice, 2nd arg: col slice)
            # Takes array from 2x slice to slice (but not including), with -1 steps
            array = array[:, :slice] | array[:, 2 * slice : slice : -1]
        if axis == "y":
            array = array[:slice, :] | array[2 * slice : slice : -1, :]
        if count is None:
            count = int(array.sum())

    print(np.array2string(array, separator="", formatter={"int": {0: " ", 1: "█"}.get}))

    return count


if __name__ == "__main__":
    from aocd.models import Puzzle

    puzzle = Puzzle(2021, 13)

    data = clean_input(puzzle.input_data)
    puzzle.answer_a = fold_origami(*data)
