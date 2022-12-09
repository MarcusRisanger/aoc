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


def traverse_graph(
    graph: dict[str, str],
    node: str = "start",
    visited: set = None,
    two_visits: bool = False,
):
    if visited is None:
        visited = set()
    result = 0
    for path in graph[node]:
        if path == "start":
            continue
        elif path == "end":
            result += 1
        elif path.islower() and path not in visited:
            # Use set union to not modify the underlying set
            # Only for the set passed through THAT recursion path
            result += traverse_graph(graph, path, visited | {path}, two_visits)
        elif path.islower() and path in visited and two_visits:
            result += traverse_graph(graph, path, visited | {path}, False)
        elif path.isupper():
            result += traverse_graph(graph, path, visited, two_visits)
    return result


if __name__ == "__main__":
    from aocd.models import Puzzle

    puzzle = Puzzle(2021, 12)
    input_data = clean_input(puzzle.input_data)

    puzzle.answer_a = traverse_graph(input_data, "start")
    puzzle.answer_b = traverse_graph(input_data, "start", two_visits=True)
