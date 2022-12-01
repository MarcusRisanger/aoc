"""
AOC 2021 Day 5: 
  - Part 1: Evaluating coordinate-based columnar/row-based line intersections on a grid
  - Part 2: Evaluating also diagonal intersections
"""

from collections import defaultdict


def clean_input(input_data: str) -> tuple[int, int, int, int]:
    return [
        list(map(int, line.replace(" -> ", ",").split(",")))
        for line in input_data.splitlines()
    ]


def track_hits(coordinates: list[list[int]], part2: bool = False):
    hits = defaultdict(int)
    for x1, y1, x2, y2 in coordinates:
        # Straights
        if x1 == x2:
            ys = sorted([int(y1), int(y2)])
            for y in range(ys[0], ys[1] + 1):
                hits[f"r{x1}c{y}"] += 1
        elif y1 == y2:
            xs = sorted([int(x1), int(x2)])
            for x in range(xs[0], xs[1] + 1):
                hits[f"r{x}c{y1}"] += 1
        # Diagonals
        elif part2 and (x1 - x2 == y1 - y2):
            steps = abs(x1 - x2) + 1
            x = min([x1, x2])
            y = min([y1, y2])
            for i in range(steps):
                hits[f"r{x+i}c{y+i}"] += 1
        elif part2 and (x1 - x2 == -(y1 - y2)):
            steps = abs(x1 - x2) + 1
            if x2 > x1:
                for i in range(steps):
                    hits[f"r{x1+i}c{y1-i}"] += 1
            else:
                for i in range(steps):
                    hits[f"r{x1-i}c{y1+i}"] += 1
    return sum(1 for v in hits.values() if v > 1)


def part1(coordinates: list[list[int]]):
    return track_hits(coordinates)


def part2(coordinates: list[list[int]]):
    return track_hits(coordinates, part2=True)


if __name__ == "__main__":
    from aocd.models import Puzzle

    # Get puzzle details and set up input
    puzzle = Puzzle(year=2021, day=5)
    coordinates = clean_input(puzzle.input_data)

    puzzle.answer_a = part1(coordinates)
    puzzle.answer_b = part2(coordinates)
