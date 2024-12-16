from queue import PriorityQueue
from collections import defaultdict


Coord = tuple[int, int]
Cost = int
Heading = tuple[int, int]
Block = str
Grid = dict[Coord, Block]


def clean_input(inp: str) -> tuple[Grid, Coord, Coord]:
    grid = {(x, y): val for y, row in enumerate(inp.splitlines()) for x, val in enumerate(row)}
    start = next(iter({k for k, v in grid.items() if v == "S"}))
    end = next(iter({k for k, v in grid.items() if v == "E"}))
    return grid, start, end


def neighbors(c: Coord, h: Heading) -> list[tuple[Coord, Heading, Cost]]:
    ns: list[tuple[Coord, Cost]] = [(h, 1), ((-h[1], h[0]), 1001), ((h[1], -h[0]), 1001)]
    return [((c[0] + h[0], c[1] + h[1]), h, cost) for h, cost in ns]


def maze(
    grid: Grid,
    start: Coord,
    heading: Heading,
    end: Coord,
) -> tuple[int, int]:
    """
    Traverse grid from start to end using Dijkstras algorithm.

    Returns cost of lowest path.
    """
    frontier: PriorityQueue[tuple[Cost, tuple[Coord, Heading, set[Coord]]]] = PriorityQueue()

    frontier.put((0, (start, heading, set())))
    cost_at: dict[tuple[Coord, Heading], Cost] = {(start, heading): 0}
    end_at: dict[Cost, set[Coord]] = defaultdict(set)

    while not frontier.empty():
        cost, (current, heading, path) = frontier.get()

        if end_at and cost > min(end_at):
            continue

        path_to_next = path | {current}

        if current == end:
            end_at[cost].update(path_to_next)
            continue

        for next, n_heading, step_cost in neighbors(current, heading):
            if grid[next] == "#":
                continue

            new_cost = cost + step_cost

            if (next, n_heading) not in cost_at or new_cost <= cost_at[(next, n_heading)]:
                cost_at[(next, n_heading)] = new_cost
                frontier.put((new_cost, (next, n_heading, path_to_next)))

    return min(end_at), len(end_at[min(end_at)])


if __name__ == "__main__":
    from aocd.models import Puzzle

    # Get puzzle details and set up input
    puzzle = Puzzle(year=2024, day=16)
    g, s, e = clean_input(puzzle.input_data)
    h = (1, 0)  # East/Right
    # Submit answers
    puzzle.answer_a, puzzle.answer_b = maze(g, s, h, e)
