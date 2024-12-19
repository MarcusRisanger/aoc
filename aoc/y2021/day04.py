"""
AOC 2021 Day 4:
  - Part 1 & 2: Solving bingo boards based on a set draw ordering.
"""

from collections import defaultdict


def clean_input(
    input_data: str,
) -> tuple[list[int], list[dict[int, str]]]:
    """Prepares the input data into a list of draws and a list of boards
    represented as dictionaries with bingo values as keys, and board
    i, j coordinate as the corresponding value strings."""
    draws = list(map(int, input_data.splitlines()[0].split(",")))

    boards = []
    for row in input_data.splitlines()[1:]:
        if row == "":
            boards.append(dict())
            i = 0  # Reset row
        else:
            for j, value in enumerate(row.split()):
                boards[-1][int(value)] = f"{i}{j}"
            i += 1  # Increment row

    return (draws, boards)


def solve_board(draws: list[int], board: dict[int, str]) -> tuple[int, int]:
    """Solves a single bingo board using the list of draws."""
    board = {k: v for k, v in board.items()}  # Create deep copy ..
    lines = defaultdict(int)
    for i_, draw in enumerate(draws):
        if draw in board:
            i, j = board.pop(draw)
            lines[f"r{i}"] += 1
            lines[f"c{j}"] += 1
            if (lines[f"r{i}"] == 5) or (lines[f"c{j}"] == 5):
                return i_, draw * sum(board.keys())


def part1(draws: list[int], boards: list[dict[int, str]]) -> int:
    """Returns the score for the first solved board."""
    return min([solve_board(draws, board) for board in boards], key=lambda x: x[0])[1]


def part2(draws: list[int], boards: list[dict[int, str]]) -> int:
    """Returns the score for the final solved board."""
    return max([solve_board(draws, board) for board in boards], key=lambda x: x[0])[1]


if __name__ == "__main__":
    from aocd.models import Puzzle

    # Get puzzle details and set up input
    puzzle = Puzzle(year=2021, day=4)
    draws, boards = clean_input(puzzle.input_data)

    puzzle.answer_a = part1(draws=draws, boards=boards)
    puzzle.answer_b = part2(draws=draws, boards=boards)
