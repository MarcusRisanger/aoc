import re
from queue import PriorityQueue

MAX = 70

Coord = tuple[int, int]


class Grid(dict):
    def neighbors(self, c: Coord) -> list[Coord]:
        return [*filter(self.get, ((c[0] + n[0], c[1] + n[1]) for n in ((0, 1), (0, -1), (1, 0), (-1, 0))))]


def clean_input(inp: str) -> tuple[Grid, tuple[Coord, ...]]:
    blockers = tuple(tuple(map(int, c)) for c in re.findall(r"(?:(\d+),(\d+))", inp))
    return Grid({(x, y): 1 for y in range(MAX + 1) for x in range(MAX + 1)}), blockers  # type: ignore


def find(grid: Grid, blockers: tuple[Coord, ...], bytes: int) -> int:  # type: ignore[return]
    """
    Traverse grid from start to end using Dijkstras algorithm.

    Returns cost of lowest path.
    """
    start, end = (0, 0), (MAX, MAX)

    frontier: PriorityQueue[tuple[int, Coord]] = PriorityQueue()

    frontier.put((0, start))
    cost_at = {start: 0}

    current_blockers = blockers[:bytes]

    while not frontier.empty():
        cost, current = frontier.get()

        if current == end:
            return cost_at[end]

        for next in grid.neighbors(current):
            if next in current_blockers:
                continue
            new_cost = cost + 1
            if next not in cost_at or new_cost < cost_at[next]:
                cost_at[next] = new_cost
                frontier.put((new_cost, next))


def ultra_lazy_part2(grid, blockers) -> str:  # type: ignore[return]
    for i in range(1024 + 1, len(blockers), 200):
        if find(grid, blockers, i) is None:
            a = i - 200
            break

    for i in range(a, len(blockers)):
        if find(grid, blockers, i) is None:
            return ",".join(map(str, blockers[i - 1]))


if __name__ == "__main__":
    from aocd.models import Puzzle

    # Get puzzle details and set up input
    puzzle = Puzzle(year=2024, day=18)
    data = clean_input(puzzle.input_data)

    # Submit answers
    puzzle.answer_a = str(find(*data, 1024))
    puzzle.answer_b = ultra_lazy_part2(*data)
