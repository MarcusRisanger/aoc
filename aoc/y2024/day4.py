from aocd.models import Puzzle

puzzle = Puzzle(2024, 4)


def clean_input(inp: str) -> dict:
    return {(x, y): val for y, row in enumerate(inp.splitlines()) for x, val in enumerate(row)}


straight = ((0, 0), (1, 0), (2, 0), (3, 0))
diag1 = ((0, 0), (1, 1), (2, 2), (3, 3))
diag2 = ((0, 0), (-1, 1), (-2, 2), (-3, 3))
down = ((0, 0), (0, 1), (0, 2), (0, 3))


def get_sub(at: tuple, dir: tuple[tuple, ...], grid: dict, search: str):
    return "".join([grid.get((at[0] + x, at[1] + y), "") for x, y in dir]) in (search, search[::-1])


grid = clean_input(puzzle.input_data)

total = 0
for i in grid:
    total += sum(get_sub(i, dir, grid, "XMAS") for dir in (straight, diag1, diag2, down))

print(f"Part 1: {total}")
puzzle.answer_a = total

p2_total = 0
for i in grid:
    if grid[i] != "A":
        continue  # No possible X-MASsing
    d1 = get_sub(i, ((-1, -1), (0, 0), (1, 1)), grid, "MAS")
    d2 = get_sub(i, ((-1, 1), (0, 0), (1, -1)), grid, "MAS")
    if d1 and d2:
        p2_total += 1

print(f"Part 2: {p2_total}")
puzzle.answer_b = p2_total
