from dataclasses import dataclass
from collections import defaultdict

Coord = tuple[int, int]
Frequency = str
Nodes = dict[Frequency, set[Coord]]


@dataclass
class Bounds:
    x_max: int
    y_max: int

    def in_bound(self, coord: Coord) -> bool:
        valid_x = 0 <= coord[0] <= self.x_max
        valid_y = 0 <= coord[1] <= self.y_max
        return valid_x and valid_y


def clean_input(inp: str) -> tuple[Nodes, Bounds]:
    """Parse into nodes and grid bounds."""
    nodes = defaultdict(set)
    for y, row in enumerate(inp.splitlines()):
        for x, val in enumerate(row):
            if val != ".":
                nodes[val].add((x, y))
    bounds = Bounds(inp.index("\n") - 1, inp.count("\n"))
    return nodes, bounds


def move(current: Coord, heading: Coord) -> Coord:
    """Move from x"""
    return current[0] + heading[0], current[1] + heading[1]


def antinodes(base: Coord, target: Coord, bounds: Bounds, n: int | None = None) -> set[Coord]:
    """Get antinodes for a base and target antenna, extending beyond the target antenna."""
    step = target[0] - base[0], target[1] - base[1]
    next = move(target, step)
    out = set()
    while bounds.in_bound(next) and (len(out) < n if n is not None else True):
        out.add(next)
        next = move(next, step)
    return out


def get_frequency_antinodes(nodes: set[Coord], bounds: Bounds, n: int | None = None) -> set[Coord]:
    """Get n or all interrelated antinodes for given set of antenna coordinates."""
    return set.union(*[antinodes(base, target, bounds, n) for base in nodes for target in nodes if base != target])


def part1(nodes: Nodes, bounds: Bounds) -> int:
    """Count unique antinode coordinates within bounds."""
    return len(set.union(*[get_frequency_antinodes(node, bounds, 1) for node in nodes.values()]))


def part2(nodes: Nodes, bounds: Bounds) -> int:
    """Count unique antinode coordinates within bounds, taking into account resonant harmonics."""
    antinodes = set.union(*[get_frequency_antinodes(node, bounds) for node in nodes.values()])
    antennas = set.union(*[n for n in nodes.values() if len(n) > 1])
    return len(antinodes | antennas)


if __name__ == "__main__":
    from aocd.models import Puzzle

    # Get puzzle details and set up input
    puzzle = Puzzle(year=2024, day=8)

    input_data = clean_input(puzzle.input_data)

    # Submit answers
    puzzle.answer_a = str(part1(*input_data))
    puzzle.answer_b = str(part2(*input_data))
