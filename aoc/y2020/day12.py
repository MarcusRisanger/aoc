Instruction = tuple[str, int]
Coordinate = tuple[int, int]
Heading = Coordinate
directions = dict(N=(0, -1), S=(0, 1), E=(1, 0), W=(-1, 0))


def clean_input(inp: str) -> list[Instruction]:
    def parse_line(arg: str):
        a, b = arg[0], arg[1:]
        return a, int(b)

    return [*map(parse_line, inp.splitlines())]


def manhattan_distance(coord: Coordinate) -> str:
    """Get Manhattan distance of current position vs. origin."""
    return str(sum(map(abs, coord)))


def turn(deg: int, heading: Heading) -> Heading:
    """
    Turns heading by `deg` degrees.
    Positive `deg`: clockwise
    Negative `deg`: anti-clockwise
    """
    x, y = heading
    return (x, y) if deg % 360 == 0 else turn(deg - 90, (-y, x))


assert turn(+90, directions["N"]) == directions["E"]
assert turn(-90, directions["N"]) == directions["W"]


def move(n: int, pos: Coordinate, heading: Heading) -> Coordinate:
    """Moves from position to heading N times."""
    x, y = pos
    dx, dy = heading
    return x + n * dx, y + n * dy


def navigate_1(instructions: list[Instruction], pos=(0, 0), heading=directions["E"]) -> str:
    for op, n in instructions:
        match op:
            case "R":  # Turn clockwise
                heading = turn(n, heading)
            case "L":  # Turn anti-clockwise
                heading = turn(-n, heading)
            case "F":
                pos = move(n, pos, heading)
            case _:
                pos = move(n, pos, directions[op])
    return manhattan_distance(pos)


def navigate_2(instructions: list[Instruction], pos=(0, 0), waypoint=(10, -1)) -> str:
    for op, n in instructions:
        match op:
            case "R":  # Turn waypoint clockwise
                waypoint = turn(n, waypoint)
            case "L":  # Turn waypoint anti-clockwise
                waypoint = turn(-n, waypoint)
            case "F":  # Drive boat waypointward (?)
                pos = move(n, pos, waypoint)
            case _:
                waypoint = move(n, waypoint, directions[op])
    return manhattan_distance(pos)


def part1(instructions: list[Instruction]) -> str:
    return navigate_1(instructions)


def part2(instructions: list[Instruction]) -> str:
    return navigate_2(instructions)


if __name__ == "__main__":
    from aocd.models import Puzzle

    puzzle = Puzzle(2020, 12)

    instructions = clean_input(puzzle.input_data)

    puzzle.answer_a = part1(instructions)
    puzzle.answer_b = part2(instructions)
