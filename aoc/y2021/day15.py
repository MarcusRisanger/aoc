from aoc.utils.grid import Grid, dijkstra, Coord


def clean_input(inp: str, p2: bool = False) -> tuple[Grid, Coord, Coord]:
    if not p2:
        grid = Grid({(x, y): int(val) for y, row in enumerate(inp.splitlines()) for x, val in enumerate(row)})
        return grid, min(grid), max(grid)

    mults = ((xm, ym) for xm in range(5) for ym in range(5))
    xmax, ymax = inp.index("\n") - 1, inp.count("\n")

    def value(val, xm, ym):
        tot = int(val) + xm + ym
        if tot > 10:
            return tot % 10 + 1  # Hacky hacky
        return max(tot % 10, 1)

    grid = dict()
    for xm, ym in mults:
        grid.update(
            {
                (x + (xmax + 1) * xm, y + (ymax + 1) * ym): value(val, xm, ym)
                for y, row in enumerate(inp.splitlines())
                for x, val in enumerate(row)
            }
        )
    return Grid(grid), min(grid), max(grid)


if __name__ == "__main__":
    from aocd.models import Puzzle

    puzzle = Puzzle(2021, 15)
    input_data = puzzle.input_data

    puzzle.answer_a = dijkstra(*clean_input(input_data))
    puzzle.answer_b = dijkstra(*clean_input(input_data, True))
