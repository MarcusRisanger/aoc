from math import prod


def paper(dims: str) -> int:
    l, w, h = [*map(int, dims.split("x"))]
    a = [(l * w), (w * h), (h * l)]
    return 2 * sum(a) + min(a)


def ribbon(dims: str) -> int:
    sides = [*map(int, dims.split("x"))]
    mins = sorted(sides)[:2]
    return sum(2 * m for m in mins) + prod(sides)


def part1(inp: str) -> int:
    return sum(map(paper, inp.splitlines()))


def part2(inp: str) -> int:
    return sum(map(ribbon, inp.splitlines()))


if __name__ == "__main__":
    from aocd.models import Puzzle

    # Get puzzle details and set up input
    puzzle = Puzzle(year=2015, day=2)

    # Submit answers
    puzzle.answer_a = str(part1(puzzle.input_data))
    puzzle.answer_b = str(part2(puzzle.input_data))
