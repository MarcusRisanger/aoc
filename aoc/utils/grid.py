from queue import PriorityQueue
from typing import Literal

Coord = tuple[int, int]
Heading = Coord
Neighbors = tuple[Coord, ...]
N4 = ((0, 1), (0, -1), (1, 0), (-1, 0))
N8 = N4 + ((1, 1), (1, -1), (-1, 1), (-1, -1))
N5 = N4 + ((0, 0))
N9 = N8 + ((0, 0))


class Grid(dict):
    def neighbors(self, c: Coord, ns: Neighbors = N4) -> list[Coord]:
        return [*filter(self.get, ((c[0] + n[0], c[1] + n[1]) for n in ns))]


def dijkstra(
    grid: Grid,
    start: Coord,
    end: Coord,
    return_type: Literal["cheapest_path", "cheapest_cost"] | None = None,
) -> int:
    """
    Traverse grid from start to end using Dijkstras algorithm.

    Returns cost of lowest path.
    """
    frontier = PriorityQueue()

    frontier.put(start, 0)
    came_from = {start: None}
    cost = {start: 0}

    while not frontier.empty():
        current: Coord = frontier.get()

        if current == end:
            break

        for next in grid.neighbors(current):
            new_cost = cost[current] + grid[next]
            if next not in cost or new_cost < cost[next]:
                cost[next] = new_cost
                frontier.put(next, new_cost)
                came_from[next] = current

    if return_type == "cheapest_cost":
        return cost[end]

    if return_type == "cheapest_path":
        path = {end}
        while True:
            prev = came_from[end]
            if prev is None:
                return path
            path.add(prev)
            end = prev

    return cost[end]
