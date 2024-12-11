from collections import defaultdict
from typing import overload

Heading = tuple[int, int]
Coord = Heading
Block = str
Grid = dict[Coord, Block]
Visited = dict[Coord, set]


def clean_input(inp: str) -> tuple[Grid, Coord]:
    """Parse into grid and find start coordinate."""
    grid = {(x, y): val for y, row in enumerate(inp.splitlines()) for x, val in enumerate(row)}
    start = next(iter({k for k, v in grid.items() if v == "^"}))
    return grid, start


def move(grid: Grid, coordinate: Coord, heading: Heading) -> tuple[Block | None, Coord]:
    """Moves along heading, returning block value and coordinate."""
    new_coord = coordinate[0] + heading[0], coordinate[1] + heading[1]
    return grid.get(new_coord), new_coord


@overload
def walk(grid: Grid, start: Coord) -> Visited: ...
@overload
def walk(grid: Grid, start: Coord, p2: bool = True) -> bool: ...
def walk(
    grid: Grid, start: Coord, p2: bool = False, heading: Coord = (0, -1), blocked: Coord | None = None
) -> Visited | bool:
    """
    Walk grid turning right when faced with an obstacle (`#`).
    For p1, return visited coordinates.
    For p2, return whether the path loops if injected coordinate is also obstacle.
    """
    seen: Visited = defaultdict(set)
    current = start
    while True:
        if p2 and heading in seen[current]:  # Loop detected! Exit.
            return True

        seen[current].add(heading)
        block, next = move(grid, current, heading)

        if block is None:  # Outside grid bounds! Exit.
            return False if p2 else seen

        if block == "#" or next == blocked:  # Turn 90 deg clockwise
            heading = -heading[1], heading[0]
            continue

        current = next  # Move along


def part1(grid: Grid, start: Coord) -> int:
    """Find how many tiles guard will walk on."""
    return len(walk(grid, start))


def part2(grid: Grid, start: Coord) -> int:
    """Check how many choices for guard looping, if one point in path is blocked."""
    return sum(walk(grid, start, p2=True, blocked=coord) for coord in walk(grid, start) if coord != start)


if __name__ == "__main__":
    from aocd.models import Puzzle

    # Get puzzle details and set up input
    puzzle = Puzzle(year=2024, day=6)
    input_data = clean_input(puzzle.input_data)

    # Submit answers
    puzzle.answer_a = str(part1(*input_data))
    puzzle.answer_b = str(part2(*input_data))
