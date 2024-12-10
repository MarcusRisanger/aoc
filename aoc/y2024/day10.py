Coord = tuple[int, int]
Height = int
Grid = dict[Coord, Height]


def clean_input(inp: str) -> Grid:
    """Parse into grid and find start coordinate."""
    return {(x, y): int(val) for y, row in enumerate(inp.splitlines()) for x, val in enumerate(row)}


def get_neighbors(current: Coord, grid: Grid) -> set[Coord]:
    """Get neighbors in all cardinal directions."""
    ns = ((0, 1), (0, -1), (1, 0), (-1, 0))
    neighbors = {(current[0] + n[0], current[1] + n[1]) for n in ns}
    return set(filter(grid.get, neighbors))


def count_paths(start: Coord, grid: Grid, ends: set[Coord]) -> int:
    """BFS for paths that increase in height by exactly 1."""
    if grid[start] == 8:
        neighbors = {n for n in get_neighbors(start, grid) if grid[n] == 9}
        ends.update(neighbors)
        return sum(1 for n in get_neighbors(start, grid) if grid[n] == 9)

    to_check = {n for n in get_neighbors(start, grid) if grid[n] - grid[start] == 1}
    if to_check:
        return sum(count_paths(cand, grid, ends) for cand in to_check)
    return 0


def parts(grid: Grid) -> tuple[int, int]:
    """Counts sum of ends encountered per start node, and total paths."""
    ends = 0
    paths = 0
    for c, val in grid.items():
        if val == 0:
            num_ends = set()
            paths += count_paths(c, grid, num_ends)
            ends += len(num_ends)
    return ends, paths


if __name__ == "__main__":
    from aocd.models import Puzzle

    # Get puzzle details and set up input
    puzzle = Puzzle(year=2024, day=10)

    input_data = clean_input(puzzle.input_data)

    part1, part2 = parts(input_data)
    # Submit answers
    puzzle.answer_a = str(part1)
    puzzle.answer_b = str(part2)
