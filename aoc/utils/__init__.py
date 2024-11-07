from colorama.ansi import AnsiBack
from colorama import Back
import os


def grid_print(grid: list[str | list[str]], clear: bool = True) -> None:
    if clear:
        os.system("cls")
    for row in grid:
        if isinstance(row, list):
            row = "".join(row)
        print(row)


def colorize(
    grid: list[list[str]], highlight: set[tuple[int, int]], color: AnsiBack = Back.GREEN
) -> list[list[str]]:
    """
    Colorize a grid with highlighted row/col coordinates.

    Parameters
    ----------
    grid : list[list[str]]
        A typical grid representation where each row is represented by a list of elements,
        and the grid is represented as a list of rows.
    highlight : set[tuple[int,int]
        A set of row-column coordinates to highlight in the printed grid.

    """

    def wrap(arg: str) -> str:
        return color + arg + Back.RESET

    for row, col in highlight:
        grid[row][col] = wrap(grid[row][col])

    return grid


def neighbors(x: int, y: int, **kw) -> list[tuple[int, int]]:
    """Returns grid neighbors.

    Default: Left/right/up/down
    Kwarg:
        - shape:
          - "box" for all adjacent neighbors
          - "diagonal" for all diagonal neighbors
          - "box-self" for all neighbors including self
    """
    up_down = [(x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1)]
    diag = [(x + 1, y + 1), (x + 1, y - 1), (x - 1, y - 1), (x - 1, y + 1)]

    if kw:
        if kw.get("shape") == "box":
            return up_down + diag
        elif kw.get("shape") == "diagonal":
            return diag
        elif kw.get("shape") == "box-self":
            return up_down + diag + [(x, y)]

    return up_down
