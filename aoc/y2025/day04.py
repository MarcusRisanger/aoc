Coord = complex


def grid(inp: str) -> set[Coord]:
    return {complex(x, y) for y, row in enumerate(inp.splitlines()) for x, val in enumerate(row) if val == "@"}


def get_neighbors(coord: Coord, grid: set[Coord]) -> int:
    neighbors = {1, -1, 1j, -1j, 1 + 1j, 1 - 1j, -1 - 1j, -1 + 1j}
    return 4 > sum(1 for n in neighbors if coord + n in grid)


def part1(grid: set[Coord]) -> int:
    return sum(get_neighbors(c, grid) for c in grid)


def part2(grid: set[Coord]) -> int:
    start = len(grid)
    while True:
        to_remove = {c for c in grid if get_neighbors(c, grid)}
        if not to_remove:
            return start - len(grid)
        grid = grid - to_remove


if __name__ == "__main__":
    from aocd.models import Puzzle

    # Get puzzle details and set up input
    puzzle = Puzzle(year=2025, day=3)
    input_data = grid(puzzle.input_data)

    # Submit answers
    puzzle.answer_a = str(part1(input_data))
    puzzle.answer_b = str(part2(input_data))
