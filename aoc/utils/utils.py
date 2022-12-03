"""
A small collection of utilities for Advent of Code puzzles.
"""


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
