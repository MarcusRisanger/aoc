from operator import add, mul
from itertools import product
from functools import partial
import re


def concat(a: int, b: int) -> int:
    """Concat on ints is no good."""
    return int(str(a) + str(b))


def process(row: str, p2: bool = False) -> bool:
    """Process returning target if row is valid else 0."""
    target, start, *rest = map(int, re.findall(r"(\d+)", row))
    operators = (add, mul, concat) if p2 else (add, mul)
    for ops in product(operators, repeat=len(rest)):
        total = start
        for i, op in enumerate(ops):
            total = op(total, rest[i])
        if total == target:
            return target
    return 0


def part1(inp: str) -> int:
    """Process rules using add, mul ops."""
    return sum(map(process, inp.splitlines()))


def part2(inp: str) -> int:
    """Process rules using add, mul, concat ops."""
    func = partial(process, p2=True)
    return sum(map(func, inp.splitlines()))


if __name__ == "__main__":
    from aocd.models import Puzzle

    # Get puzzle details and set up input
    puzzle = Puzzle(year=2024, day=7)

    # Submit answers
    puzzle.answer_a = str(part1(puzzle.input_data))
    puzzle.answer_b = str(part2(puzzle.input_data))
