"""
AOC 2021, Day 9:
   - Part 1: Check for local minimums
   - Part 2: "Fill container" type recursion
"""

from dataclasses import dataclass


@dataclass
class Coord:
    x: int
    y: int
    val: int


@dataclass
class Grid:
    g: list[list[int]]

    def __post_init__(self) -> None:
        self.R: int = len(self.g)
        self.C: int = len(self.g[0])


def clean_input(input_data: str) -> Grid:
    return Grid([list(map(int, line)) for line in input_data.splitlines()])


def get_neighbors(c: Coord, g: Grid) -> list[Coord]:
    """Neighbors in this case are only up/down/left/right"""
    n = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    gen = (
        (c.x + x, c.y + y)
        for x, y in n
        if (0 <= c.x + x < g.R) and (0 <= c.y + y < g.C)
    )
    for x, y in gen:
        yield x, y


def part1(grid: Grid) -> tuple[int, list[Coord]]:
    """Returns the total risk level and a list of trough coordinates."""
    troughs: list[Coord] = []
    for x in range(grid.R):
        for y in range(grid.C):
            c = Coord(x, y, grid.g[x][y])
            if all(c.val < grid.g[n_x][n_y] for n_x, n_y in get_neighbors(c, grid)):
                troughs.append(c)

    return sum(c.val + 1 for c in troughs), troughs


def part2(grd: Grid, coords: list[list[int]], troughs: list[Coord]):
    def get_basin_size(grid: Grid, start: Coord):
        pass

    pass


if __name__ == "__main__":
    from aocd.models import Puzzle

    puzzle = Puzzle(year=2021, day=9)
    height_map = clean_input(puzzle.input_data)

    puzzle.answer_a, troughs = part1(*height_map)
    # puzzle.answer_b = part2(*height_map, troughs)
