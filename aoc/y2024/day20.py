Coord = tuple[int, int]
Grid = set[Coord]
Step = int
Path = dict[Coord, Step]


def clean_input(inp: str) -> tuple[Grid, Coord, Coord]:  # type: ignore[return]
    coords: set[Coord] = set()
    start = end = None
    for y, row in enumerate(inp.splitlines()):
        for x, val in enumerate(row):
            if val == "S":
                start = (x, y)
            elif val == "E":
                end = (x, y)
            elif val == ".":
                coords.add((x, y))
    return coords, start, end


def get_next(coord: Coord, grid: Grid, path: Path) -> Coord | None:
    ns = [(coord[0] + n[0], coord[1] + n[1]) for n in ((0, 1), (0, -1), (1, 0), (-1, 0))]
    cand = [n for n in ns if n in grid and n not in path]
    return cand[0] if cand else None


def get_path(grid: Grid, start: Coord, end: Coord) -> Path:
    grid = grid.copy()
    current = start
    path = dict()
    step = 0
    while current not in path:
        path[current] = step
        current = get_next(current, grid, path) or end
        step += 1

    return path


def part1(path: Path) -> int:
    count = 0
    for c in path:
        cands = ((c[0] + n[0], c[1] + n[1]) for n in ((0, 2), (0, -2), (2, 0), (-2, 0)))
        for n in [*filter(path.get, cands)]:
            gap = path[n] - path[c] - 2
            if gap >= 100:
                count += 1
    return count


def part2(path: Path) -> int:
    count = 0
    for c in path:
        cands = ((c[0] + i, c[1] + j) for i in range(-20, 21) for j in range(-20, 21) if abs(i) + abs(j) <= 20)
        for n in set([*filter(path.get, cands)]):
            gap = path[n] - path[c] - sum([abs(c[0] - n[0]), abs(c[1] - n[1])])
            if gap >= 100:
                count += 1
    return count


if __name__ == "__main__":
    from aocd.models import Puzzle

    # Get puzzle details and set up input
    puzzle = Puzzle(year=2024, day=20)
    data = clean_input(puzzle.input_data)
    path = get_path(*data)

    # Submit answers
    puzzle.answer_a = str(part1(path))
    puzzle.answer_b = str(part2(path))
