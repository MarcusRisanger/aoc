def fuel(x: int | str) -> int:
    return int(x) // 3 - 2


def fuel_buffered(mass: str | int) -> int:
    _fuel = 0
    while True:
        mass = fuel(mass)
        if mass <= 0:
            return _fuel
        _fuel += mass


def part1(inp: str) -> str:
    return str(sum(map(fuel, inp.splitlines())))


def part2(inp: str) -> str:
    return str(sum(map(fuel_buffered, inp.splitlines())))


if __name__ == "__main__":
    from aocd.models import Puzzle

    # Get puzzle details and set up input
    puzzle = Puzzle(year=2019, day=1)

    # Submit answers
    puzzle.answer_a = part1(puzzle.input_data)
    puzzle.answer_b = part2(puzzle.input_data)
