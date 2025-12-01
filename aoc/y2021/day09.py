"""
AOC 2021, Day 9:
   - Part 1: Check for local minimums
   - Part 2: "Fill container" type recursion
"""

from dataclasses import dataclass
from collections.abc import Generator
from math import prod
from aoc.utils import neighbors as get_n


@dataclass
class Coord:
    x: int
    y: int
    val: int

    def __hash__(self) -> int:
        return hash(repr(self))


@dataclass
class Grid:
    g: list[list[int]]

    def __post_init__(self) -> None:
        self.R: int = len(self.g)
        self.C: int = len(self.g[0])


def clean_input(input_data: str) -> Grid:
    return Grid([list(map(int, line)) for line in input_data.splitlines()])


def get_neighbors(c: Coord, g: Grid) -> Generator[Coord]:
    """Neighbors in this case are only up/down/left/right"""
    gen = ((x, y) for x, y in get_n((c.x, c.y)) if (0 <= x < g.R) and (0 <= y < g.C))
    for x, y in gen:
        yield Coord(x, y, g.g[x][y])


def get_basin_size(grid: Grid, start: Coord, visited: set = None, queue: set = None):
    if visited is None:
        visited = set()
    if queue is None:
        queue = set()
    if start in visited:
        queue.remove(start)
    else:
        visited.add(start)
        queue.update(
            n for n in get_neighbors(start, grid) if (n not in visited) and (n.val < 9)
        )
        if not queue:
            return len(visited)
        get_basin_size(grid, queue.pop(), visited, queue)
    return len(visited)


def part1(grid: Grid) -> tuple[int, list[Coord]]:
    """Returns the total risk level and a list of trough coordinates."""
    troughs: list[Coord] = []
    for x in range(grid.R):
        for y in range(grid.C):
            c = Coord(x, y, grid.g[x][y])
            if all(c.val < grid.g[n.x][n.y] for n in get_neighbors(c, grid)):
                troughs.append(c)

    return sum(c.val + 1 for c in troughs), troughs


def part2(grid: Grid, troughs: list[Coord]):
    return prod(sorted(list(map(lambda i: get_basin_size(grid, i), troughs)))[-3:])


if __name__ == "__main__":
    from aocd.models import Puzzle

    puzzle = Puzzle(year=2021, day=9)
    height_map = clean_input(puzzle.input_data)

    puzzle.answer_a, troughs = part1(height_map)
    puzzle.answer_b = part2(height_map, troughs)


## Alternative (magic) solution by /u/4HbQ:
# from math import prod

# height = {(x,y):int(h) for y,l in enumerate(open(0))
#                        for x,h in enumerate(l.strip())}

# def neighbours(x, y):
#   return filter(lambda n: n in height,  # remove points
#     [(x,y-1),(x,y+1),(x-1,y),(x+1,y)])  #  outside grid

# def is_low(p):
#   return all(height[p] < height[n]
#     for n in neighbours(*p))

# low_points = list(filter(is_low, height))
# print(sum(height[p]+1 for p in low_points))

# def count_basin(p):
#   if height[p] == 9: return 0  # stop counting at ridge
#   del height[p]                # prevent further visits
#   return 1+sum(map(count_basin, neighbours(*p)))

# basins = [count_basin(p) for p in low_points]
# print(prod(sorted(basins)[-3:]))
