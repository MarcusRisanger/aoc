from collections.abc import Callable
from aoc.utils import extract_neighbors

Status = str
Chair = tuple[int, int]
Layout = dict[Chair, Status]
AdjacencyFunc = Callable[[Chair, Layout], int]


def clean_input(inp: str) -> Layout:
    return {
        (x, y): val
        for y, row in enumerate(inp.splitlines())
        for x, val in enumerate(row)
    }


def count_adjacent_occupied(chair: Chair, layout: Layout) -> int:
    """
    Adjacency function for part 1.
    Counts occupied seats in the "box shape" around the supplied Chair.
    """
    return [*map(layout.get, extract_neighbors(chair, layout, shape="box"))].count("#")


def is_first_visible_seat_occupied(
    chair: Chair, layout: Layout, vector: tuple[int, int]
) -> bool:
    """
    Goes from a chair (point) along a vector (direction) to determine occupancy.
    """
    while True:
        chair = chair[0] + vector[0], chair[1] + vector[1]
        at_point = layout.get(chair)

        if at_point is None:
            return False  # Outside of grid
        if at_point == ".":
            continue  # Floors can be skipped
        return at_point == "#"  # Is occupied


def count_line_of_sight(chair: Chair, layout: Layout) -> int:
    """
    Adjacency function for part 2.
    Counts occupied chairs in each line of sight direction.
    """
    directions = (
        (-1, -1),  # NW
        (0, -1),  # N
        (1, -1),  # NE
        (1, 0),  # E
        (1, 1),  # SE
        (0, 1),  # S
        (-1, 1),  # SW
        (-1, 0),  # W
    )
    return sum(
        is_first_visible_seat_occupied(chair, layout, vector) for vector in directions
    )


def cycle(layout: Layout, adjacency_func: AdjacencyFunc, limit: int) -> Layout:
    """
    Cycles seating arrangements until steady state, and returns the layout at that time.
    """
    while True:
        has_changed = False
        new_layout = layout.copy()
        for chair in layout:
            if layout[chair] == "L" and adjacency_func(chair, layout) == 0:
                new_layout[chair] = "#"
                has_changed = True
            elif layout[chair] == "#" and adjacency_func(chair, layout) >= limit:
                new_layout[chair] = "L"
                has_changed = True

        if not has_changed:
            return new_layout

        layout = new_layout


def occupied_seats(layout: Layout) -> str:
    return str(sum(1 for v in layout.values() if v == "#"))


def part1(layout: Layout) -> str:
    layout = cycle(layout, adjacency_func=count_adjacent_occupied, limit=4)
    return occupied_seats(layout)


def part2(layout: Layout) -> str:
    layout = cycle(layout, adjacency_func=count_line_of_sight, limit=5)
    return occupied_seats(layout)


if __name__ == "__main__":
    from aocd.models import Puzzle

    puzzle = Puzzle(2020, 11)
    layout = clean_input(puzzle.input_data)

    puzzle.answer_a = part1(layout)
    puzzle.answer_b = part2(layout)
