"""
AOC 2021 Day 5: 
  - Part 1: Evaluating coordinate-based columnar/row-based line intersections on a grid
  - Part 2: Evaluating also diagonal intersections
"""

from collections import defaultdict
from itertools import zip_longest


def clean_input(input_data: str) -> tuple[int, int, int, int]:
    return [
        list(map(int, line.replace(" -> ", ",").split(",")))
        for line in input_data.splitlines()
    ]


def get_hits(x1: int, x2: int) -> list[int]:
    """Output steps based on one-dimensional coordinate difference."""
    # To handle cases where the line is drawn in negative direction
    sort = 1 if x2 > x1 else -1
    # To set the proper arguments for range
    x1, x2 = min([x1, x2]), max([x1, x2])
    return [*range(x1, x2 + 1)][::sort]


def track_hits(coordinates: list[list[int]], part2: bool = False):
    """Tracking hits of the diff coordinates."""
    hits = defaultdict(int)
    for x1, y1, x2, y2 in coordinates:
        if x1 == x2 or y1 == y2 or part2:
            x_hits, y_hits = get_hits(x1, x2), get_hits(y1, y2)
            padding = x1 if len(x_hits) == 1 else y1
            for hit in zip_longest(x_hits, y_hits, fillvalue=padding):
                hits[hit] += 1

    return sum(1 for v in hits.values() if v > 1)


def part1(coordinates: list[list[int]]) -> int:
    """Returns number of coordinate points with line overlaps
    for straight lines only."""
    return track_hits(coordinates)


def part2(coordinates: list[list[int]]) -> int:
    """Returns number of coordinate points with line overlaps,
    for straight and diagonal lines."""
    return track_hits(coordinates, part2=True)


if __name__ == "__main__":
    from aocd.models import Puzzle

    # Get puzzle details and set up input
    puzzle = Puzzle(year=2021, day=5)
    coordinates = clean_input(puzzle.input_data)

    puzzle.answer_a = part1(coordinates)
    puzzle.answer_b = part2(coordinates)
