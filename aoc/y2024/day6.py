from collections import defaultdict
from typing import overload

Heading = tuple[int, int]
Coordinate = Heading
Block = str
Grid = dict[Coordinate, Block]


def clean_input(inp: str) -> Grid:
    return {(x, y): val for y, row in enumerate(inp.splitlines()) for x, val in enumerate(row)}


def get_start(grid: Grid) -> Coordinate:
    return next(iter({k for k, v in grid.items() if v == "^"}))


def move(grid: Grid, coordinate: Coordinate, heading: Heading) -> tuple[Block | None, Coordinate]:
    """Moves along heading, returning block value and coordinate."""
    new_coord = coordinate[0] + heading[0], coordinate[1] + heading[1]
    return grid.get(new_coord), new_coord


def substitute(grid: Grid, coordinate: Coordinate) -> Grid:
    """Get copy of grid with a coordinate substituted."""
    grid = grid.copy()
    grid[coordinate] = "#"
    return grid


@overload
def walk(grid: Grid) -> dict[Coordinate, list[Heading]]: ...
@overload
def walk(grid: Grid, p2: bool = True) -> bool: ...
def walk(grid: Grid, p2: bool = False, heading: Coordinate = (0, -1)) -> dict[Coordinate, list[Heading]] | bool:
    seen: dict[Coordinate, list[Heading]] = defaultdict(list)
    current = get_start(grid)
    while current:
        if p2 and heading in seen[current]:  # Loop detected! Exit.
            return True

        seen[current].append(heading)
        block, next = move(grid, current, heading)

        if block is None:  # No loop! Exit.
            return False if p2 else seen
        elif block == "#":  # Turn 90 deg clockwise
            heading = -heading[1], heading[0]
            continue
        else:  # Move along
            current = next


def part1(grid: Grid) -> int:
    return len(walk(grid))


def part2(grid: Grid) -> int:
    seen = walk(grid)
    # Can't put obstacle in starting point
    seen.pop(get_start(grid))
    return sum(walk(substitute(grid, coord), True) for coord in seen)


if __name__ == "__main__":
    from aocd.models import Puzzle

    # Get puzzle details and set up input
    puzzle = Puzzle(year=2024, day=6)
    input_data = clean_input(puzzle.input_data)
    # Submit answers
    puzzle.answer_a = str(part1(input_data))
    puzzle.answer_b = str(part2(input_data))
