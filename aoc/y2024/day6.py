from collections import defaultdict
from typing import overload

Heading = tuple[int, int]
Coordinate = Heading
Block = str
Grid = dict[Coordinate, Block]


def clean_input(inp: str) -> Grid:
    return {(x, y): val for y, row in enumerate(inp.splitlines()) for x, val in enumerate(row)}


def get_start(grid: Grid) -> Coordinate:
    """Find coordinate of starting point (`^`) in grid."""
    return next(iter({k for k, v in grid.items() if v == "^"}))


def move(grid: Grid, coordinate: Coordinate, heading: Heading) -> tuple[Block | None, Coordinate]:
    """Moves along heading, returning block value and coordinate."""
    new_coord = coordinate[0] + heading[0], coordinate[1] + heading[1]
    return grid.get(new_coord), new_coord


def block(grid: Grid, coordinate: Coordinate) -> Grid:
    """Get copy of grid with a blocker (`#`) inserted at coordinate."""
    return {k: "#" if k == coordinate else v for k, v in grid.items()}


@overload
def walk(grid: Grid) -> dict[Coordinate, list[Heading]]: ...
@overload
def walk(grid: Grid, p2: bool = True) -> bool: ...
def walk(grid: Grid, p2: bool = False, heading: Coordinate = (0, -1)) -> dict[Coordinate, list[Heading]] | bool:
    """
    Walk grid turning right when faced with an obstacle (`#`).
    For p1, return visited coordinates.
    For p2, return whether the path loops.
    """
    seen: dict[Coordinate, list[Heading]] = defaultdict(list)
    current = get_start(grid)
    while True:
        if p2 and heading in seen[current]:  # Loop detected! Exit.
            return True

        seen[current].append(heading)
        block, next = move(grid, current, heading)

        if block is None:  # Outside grid bounds! Exit.
            return False if p2 else seen

        elif block == "#":  # Turn 90 deg clockwise
            heading = -heading[1], heading[0]
            continue
        else:  # Move along
            current = next


def part1(grid: Grid) -> int:
    """Find how many tiles guard will walk on."""
    return len(walk(grid))


def part2(grid: Grid) -> int:
    """Check how many choices for guard looping, if one point in path is blocked."""
    guard_path = {k: v for k, v in walk(grid).items() if k != get_start(grid)}  # Can't put obstacle in starting point
    return sum(walk(block(grid, coord), True) for coord in guard_path)


if __name__ == "__main__":
    from aocd.models import Puzzle

    # Get puzzle details and set up input
    puzzle = Puzzle(year=2024, day=6)
    input_data = clean_input(puzzle.input_data)
    # Submit answers
    puzzle.answer_a = str(part1(input_data))
    puzzle.answer_b = str(part2(input_data))
