"""
AOC 2021, Day 12:
  - Graph creation!
  - Graph traversal.
"""
from collections import defaultdict


def clean_input(input_data: str) -> dict[str, str]:
    """Generates list of possible paths from input data."""
    graph = defaultdict(set)
    for row in input_data.splitlines():
        x, y = row.split("-")
        graph[x].add(y)
        graph[y].add(x)
    return graph


def walk_graph(
    graph: dict[str, str],
    node: str = "start",
    visited: list = [],
    one_visit: bool = True,
):
    """Returns the result for walking the graph. If function does not terminate, it
    recursively calls the function for each node neighbor of the graph."""
    if node == "end":
        return 1
    elif node in visited:
        if node == "start":
            return 0
        if node.islower():
            # If we are only visiting each lowercase cave once, we return zero if we encounter
            # a lower case cave that is in visited. Else we change our recursive call argument.
            if one_visit:
                return 0
            else:
                one_visit = True
    return sum(walk_graph(graph, n, visited + [node], one_visit) for n in graph[node])


if __name__ == "__main__":
    from aocd.models import Puzzle

    puzzle = Puzzle(2021, 12)
    input_data = clean_input(puzzle.input_data)

    puzzle.answer_a = walk_graph(input_data)
    puzzle.answer_b = walk_graph(input_data, one_visit=False)
