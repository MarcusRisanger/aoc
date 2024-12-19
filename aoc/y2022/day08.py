from dataclasses import dataclass


@dataclass
class Grid:
    g: list[list[int]]
    R: int
    C: int


def clean_input(input_data: str) -> Grid:
    rows = input_data.splitlines()
    return Grid([list(map(int, i)) for i in rows], len(rows) - 1, len(rows[0]) - 1)


def evaluate_tree(grid: Grid, x: int, y: int) -> tuple[bool, int]:
    tree_height = grid.g[x][y]
    visible = False
    scenic_score = 1
    for dx, dy in ((-1, 0), (1, 0), (0, -1), (0, 1)):
        # Instantiate start point from given coordinate
        xx, yy = x, y
        trees_seen = 0
        # Walk toward edge
        while 0 < xx < grid.R and 0 < yy < grid.C:
            trees_seen += 1

            # If tree in next direction is as tall or taller, break
            if grid.g[xx + dx][yy + dy] >= tree_height:
                break

            # Increment
            xx += dx
            yy += dy

        # If we reached beyond the edge
        if xx == 0 or grid.R == xx or yy == 0 or grid.C == yy:
            visible = True
        scenic_score *= trees_seen
    return visible, scenic_score


def solve(grid: Grid):
    coords = ((x, y) for x in range(len(grid.g)) for y in range(len(grid.g[0])))
    results = list(map(lambda i: evaluate_tree(grid, *i), coords))
    return sum(i[0] for i in results), max(i[1] for i in results)


if __name__ == "__main__":
    from aocd.models import Puzzle

    # Get puzzle details and set up input
    puzzle = Puzzle(year=2022, day=8)
    input_data = clean_input(puzzle.input_data)

    # Submit answers
    puzzle.answer_a, puzzle.answer_b = solve(input_data)
