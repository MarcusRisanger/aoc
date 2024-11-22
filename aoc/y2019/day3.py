from collections import Counter

directions = dict(U=(0, -1), D=(0, 1), L=(-1, 0), R=(1, 0))

Instruction = str
Wire = list[Instruction]
Point = tuple[int, int]


def clean_input(inp: str) -> list[Wire]:
    return [row.split(",") for row in inp.splitlines()]


def go(pos: Point, dir: Point) -> Point:
    return pos[0] + dir[0], pos[1] + dir[1]


def draw_wires(wires: list[Wire]) -> dict[Point, int]:
    counter: dict = Counter()  # For tracking all visited coordinates
    for wire in wires:
        wire_points: set[Point] = set()  # For tracking visited coordinates for this wire
        pos = (0, 0)
        for wire_element in wire:
            direction, n = wire_element[0], wire_element[1:]
            for _ in range(int(n)):
                pos = go(pos, directions[direction])
                wire_points.add(pos)
        counter.update(wire_points)
    return counter


def part1(wires: list[Wire]) -> str:
    crosses_at = [coord for coord, val in draw_wires(wires).items() if val > 1]
    return str(min(sum(map(abs, coord)) for coord in crosses_at))


if __name__ == "__main__":
    from aocd.models import Puzzle

    # Get puzzle details and set up input
    puzzle = Puzzle(year=2019, day=3)

    wires = clean_input(puzzle.input_data)

    # Submit answers
    puzzle.answer_a = part1(wires)
