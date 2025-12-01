from __future__ import annotations

from dataclasses import dataclass

from colorama import Back
from re import findall

from aoc.utils import colorize, grid_print


@dataclass(frozen=True, slots=True)
class Coord:
    row: int
    col: int

    def get_neighbor(self, move: Coord) -> Coord:
        return Coord(self.row + move.row, self.col + move.col)


def transform_input(inp: str) -> list[str]:
    return inp.splitlines()


def get_pipe_symbol(inp: list[str], coord: Coord):
    """Get pipe symbol at coordinate."""
    if 0 <= coord.row < len(inp) and 0 <= coord.col < len(inp[0]):
        return inp[coord.row][coord.col]


def get_start_coord(inp: list[str]) -> Coord:  # type: ignore[return]
    """Get coordinate for 'S' pipe element."""
    for r in range(len(inp)):
        for c in range(len(inp[0])):
            if inp[r][c] == "S":
                return Coord(r, c)


def get_first_move(pipes: list[str], start_coord: Coord) -> Coord:  # type: ignore[return]
    """Get first move from 'S' pipe element."""
    valid_pipes: dict[Coord, list[str]] = {
        Coord(1, 0): ["|", "L", "J"],  # Go down
        Coord(-1, 0): ["|", "F", "7"],  # Go up
        Coord(0, 1): ["-", "J", "7"],  # Go right
        Coord(0, -1): ["-", "L", "F"],  # Go left
    }
    for move, valid_pipe_symbols in valid_pipes.items():
        move_to = start_coord.get_neighbor(move)
        if get_pipe_symbol(pipes, move_to) in valid_pipe_symbols:
            return move_to


def get_valid_moves(current_pipe: str, current_coordinate: Coord) -> list[Coord]:
    """
    Get valid moves based on pipe symbol and current coordinate.

    Each symbol can connect to the next pipe element in two directions.
    """
    legal_moves = {
        "|": (Coord(-1, 0), Coord(1, 0)),  # Up/down
        "-": (Coord(0, -1), Coord(0, 1)),  # Left/right
        "L": (Coord(-1, 0), Coord(0, 1)),  # Up/right
        "F": (Coord(1, 0), Coord(0, 1)),  # Down/right
        "J": (Coord(-1, 0), Coord(0, -1)),  # Up/left
        "7": (Coord(1, 0), Coord(0, -1)),  # Down/left
    }[current_pipe]
    return [current_coordinate.get_neighbor(move) for move in legal_moves]


def get_next_move(moves: list[Coord], seen: set[Coord]) -> Coord | None:
    """
    Get next move from a list of valid moves.

    Only one will be valid, the other will be already visited.
    """
    for move in moves:
        if move not in seen:
            return move
    return None


def pipe_replacer(pipes: list[str], seen: set[Coord]):
    """Some fun - replace pipe symbols with box drawing symbols."""
    pipe_copy = [list(p) for p in pipes]
    replacers = {
        "-": "\u2500",
        "|": "\u2502",
        "F": "\u256d",
        "7": "\u256e",
        "J": "\u256f",
        "L": "\u2570",
        "S": "S",
    }

    for pipe in seen:
        pipe_copy[pipe.row][pipe.col] = replacers[pipe_copy[pipe.row][pipe.col]]
    return ["".join(p) for p in pipe_copy]


def draw(
    pipes: list[str], seen: set[Coord], enclosed: set[Coord] | None = None
) -> None:
    draw_pipes = [list(p) for p in pipe_replacer(pipes, seen)]
    to_draw = colorize(
        draw_pipes, {(c.row, c.col) for c in seen}
    )  # Highlighting pipe system

    if enclosed is not None:
        to_draw = colorize(
            to_draw, {(c.row, c.col) for c in enclosed}, color=Back.RED
        )  # Highlighting enclosed
    grid_print(to_draw)  # To stdout


def get_pipe_elements(pipes: list[str], start_coord: Coord) -> set[Coord]:
    seen = {start_coord}
    current = get_first_move(pipes, start_coord)
    while True:
        seen.add(current)
        # colorize(pipes, {(c.row, c.col) for c in seen}) # Needs: from aoc.utils import colorize
        current_symbol = get_pipe_symbol(pipes, current)
        possible_moves = get_valid_moves(current_symbol, current)
        next_coord = get_next_move(possible_moves, seen)

        if next_coord is None:
            return seen
        current = next_coord


def traverse_pipe(pipes: list[str]):
    start = get_start_coord(pipes)
    return get_pipe_elements(pipes, start)


def strip_grid(pipes: list[str], seen: set[Coord]) -> list[str]:
    grid = [list(p) for p in pipes]
    for r in range(len(grid)):
        for c in range(len(grid[0])):
            if Coord(r, c) not in seen:
                grid[r][c] = "."
    return ["".join(row) for row in grid]


def count_enclosed(
    grid: list[str], seen: set[Coord], draw_grid: bool = False
) -> set[Coord]:
    grid = strip_grid(grid, seen)

    enclosed = set()
    for r, row in enumerate(grid):
        for c, val in enumerate(row):
            if val == "." and len(findall("[S|7F]", row[:c])) % 2 != 0:
                enclosed.add(Coord(r, c))

    if draw_grid:
        draw(grid, seen, enclosed)

    return enclosed


def part1(inp: str) -> str:
    pipes = transform_input(inp)
    return str(len(traverse_pipe(pipes)) // 2)


def part2(inp: str) -> str:
    pipes = transform_input(inp)
    seen = traverse_pipe(pipes)
    val = len(
        count_enclosed(
            pipes,
            seen,
            # True, # For printing result
        )
    )
    return str(val)


if __name__ == "__main__":
    from aocd.models import Puzzle

    # Get puzzle details and set up input
    puzzle = Puzzle(year=2023, day=10)

    # Submitting answers
    puzzle.answer_a = part1(puzzle.input_data)
    puzzle.answer_b = part2(puzzle.input_data)
