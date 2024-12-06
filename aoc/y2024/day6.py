from collections import defaultdict

Heading = tuple[int, int]
Coordinate = Heading
Block = str
Grid = dict[Coordinate, Block]


def clean_input(inp: str) -> Grid:
    return {(x, y): val for y, row in enumerate(inp.splitlines()) for x, val in enumerate(row)}


def turn(heading: Heading) -> Heading:
    """Turns 90 deg right."""
    return -heading[1], heading[0]


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


def walk(grid: Grid, p2: bool = False) -> dict[Coordinate] | bool:
    current = get_start(grid)
    heading = (0, -1)
    seen: dict[Coordinate, list[Heading]] = defaultdict(list)
    while current:
        if p2 and heading in seen[current]:  # Loop detected
            return True
        seen[current].append(heading)

        block, next = move(grid, current, heading)

        if block is None:  # No loop!
            return False if p2 else seen
        elif block == "#":
            heading = turn(heading)
            continue
        else:
            current = next


def part1(grid: Grid) -> int:
    return len(walk(grid))


def part2(grid: Grid):
    seen = walk(grid)
    start = get_start(grid)

    # Can't put obstacle in starting point
    seen.pop(start)

    loops = 0
    for coord in seen:
        new_grid = substitute(grid, coord)
        loops += walk(new_grid, p2=True)
    return loops


if __name__ == "__main__":
    from aocd.models import Puzzle

    # Get puzzle details and set up input
    puzzle = Puzzle(year=2024, day=6)
    input_data = clean_input(puzzle.input_data)
    # Submit answers
    puzzle.answer_a = str(part1(input_data))
    puzzle.answer_b = str(part2(input_data))
