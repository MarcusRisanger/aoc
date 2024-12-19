from collections import Counter

directions = dict(U=(0, -1), D=(0, 1), L=(-1, 0), R=(1, 0))

Instruction = str
WireInstruction = list[Instruction]
Point = tuple[int, int]
Step = int
Wire = dict[Point, Step]


def clean_input(inp: str) -> list[WireInstruction]:
    return [row.split(",") for row in inp.splitlines()]


def go(pos: Point, dir: Point) -> Point:
    """Move once from `pos` in a direction `dir`."""
    return pos[0] + dir[0], pos[1] + dir[1]


def parse_wires(wires: list[WireInstruction]) -> list[Wire]:
    """
    Parse wire instructions into a list of `Wire` objects.

    A `Wire` object is a dictionary with coordinate `Point` as keys,
    and the value is the `Step` for the wire to reach that point.

    If a `Wire` crosses itself, the lowest `Step` is kept.
    """
    all_wires: list[dict[Point, Step]] = list()  # For tracking all visited coordinates
    for wire in wires:
        wire_points: dict[Point, Step] = dict()  # For tracking visited coordinates for this wire
        pos = (0, 0)
        step = 0
        for wire_element in wire:
            direction, n = wire_element[0], wire_element[1:]
            for _ in range(int(n)):
                step += 1
                pos = go(pos, directions[direction])
                if pos not in wire_points:
                    wire_points[pos] = step
        all_wires.append(wire_points)
    return all_wires


def get_crosses(wires: list[Wire]) -> list[Point]:
    """For a list of wires, get all coordinates where any separate wires cross."""
    counter = Counter([key for wire in wires for key in wire.keys()])
    return [k for k, v in counter.items() if v > 1]


def get_min_path_length(point: Point, wires: list[Wire]) -> int:
    """For a point and list of wires, get the lowest step count for any two wires to reach point."""
    steps = sorted(set(filter(None, (wire.get(point) for wire in wires))))
    return steps[0] + steps[1]


def get_wires_crosses(wires: list[WireInstruction]) -> tuple[list[Wire], list[Point]]:
    all_wires = parse_wires(wires)
    return all_wires, get_crosses(wires)


def part1(wires: list[WireInstruction]) -> str:
    """Get manhattan distance to closest wire crossing relative to origin (0,0)"""
    _, crosses = get_wires_crosses(wires)
    return str(min(sum(map(abs, coord)) for coord in crosses))


def part2(wires: list[WireInstruction]) -> str:
    """Get lowest number of steps from origin for two wires to cross."""
    all_wires, crosses = get_wires_crosses(wires)
    return str(min(get_min_path_length(p, all_wires) for p in crosses))


if __name__ == "__main__":
    from aocd.models import Puzzle

    # Get puzzle details and set up input
    puzzle = Puzzle(year=2019, day=3)

    wires = clean_input(puzzle.input_data)

    # Submit answers
    puzzle.answer_a = part1(wires)
    puzzle.answer_b = part2(wires)
