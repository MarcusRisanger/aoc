from string import ascii_lowercase as lc


def clean_input(input_data: str):
    """Cleans input data to node dictionary, start and stop node."""
    nodes = dict()
    a_nodes = list()
    specials = {"E": 25, "S": 0}
    for x, line in enumerate(input_data.splitlines()):
        for y, val in enumerate(line):
            if val == "S":
                start = [(x, y)]
            if val == "E":
                stop = (x, y)
            if val == "a":
                a_nodes.append((x, y))
            nodes[(x, y)] = lc.index(val) if val in lc else specials[val]
    return nodes, start, stop, a_nodes


def get_neighbors(x, y, nodes: dict):
    """Yields neighbors (up, down, left, right)
    where grid value is same or up by 1."""
    neighbors = ((1, 0), (-1, 0), (0, 1), (0, -1))
    R, C = max(nodes)
    for dx, dy in neighbors:
        if (0 <= x + dx <= R) and (0 <= y + dy <= C):
            if nodes[(x + dx, y + dy)] - nodes[(x, y)] < 2:
                yield x + dx, y + dy


def climb(nodes: dict, start: list[tuple[int, int]], stop: tuple[int, int]):
    """DFS from starting points to target - returns fewest steps required."""
    visited = {i: 0 for i in start}
    queue = [i for i in start]
    while queue:
        node = queue.pop(0)
        current_step = visited[node]
        for dx, dy in get_neighbors(*node, nodes):
            if (dx, dy) == stop:
                return current_step + 1
            if (dx, dy) not in visited:
                queue.append((dx, dy))
                visited[(dx, dy)] = current_step + 1


def find_scenic_climb(nodes, start, stop, a_nodes):
    """Special case where all `a`-nodes are entered as starting points.
    Calculates the shortest path to stop for any node."""
    return climb(nodes, start + a_nodes, stop)


if __name__ == "__main__":
    from aocd.models import Puzzle

    puzzle = Puzzle(2022, 12)

    input_data = clean_input(puzzle.input_data)

    puzzle.answer_a = climb(*input_data[:-1])
    puzzle.answer_b = find_scenic_climb(*input_data)
