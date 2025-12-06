import re
from math import prod
from typing import Iterable

from typing_extensions import Callable

Args = list[Callable[[Iterable], int]]
Nums = TNums = list[list[int]]


def clean_input(inp: str) -> tuple[Args, Nums, TNums]:
    lines = inp.splitlines()
    args: Args = [{"+": sum, "*": prod}[i] for i in re.findall(r"\S", lines[-1])]
    rows: Nums = [[int(d) for d in re.findall(r"(\d+)", row)] for row in lines[:-1]]

    # Transposing
    new = []
    for y, row in enumerate(lines[:-1]):
        for x, val in enumerate(row):
            if y == 0:
                new.append([])
            if val != " ":
                new[x].append(val)

    transposed: TNums = [[]]
    for row in new:
        if not row:
            transposed.append([])
            continue
        transposed[-1].append(int("".join(row)))
    return args, rows, transposed


def part1(args, rows) -> int:
    return sum(args[i](r[i] for r in rows) for i in range(len(args)))


def part2(args, transposed) -> int:
    return sum(args[i](r) for i, r in enumerate(transposed))


if __name__ == "__main__":
    from aocd.models import Puzzle

    # Get puzzle details and set up input
    puzzle = Puzzle(year=2025, day=6)
    input_data = puzzle.input_data

    args, nums, tnums = clean_input(input_data)

    # Submit answers
    puzzle.answer_a = str(part1(args, nums))
    puzzle.answer_b = str(part2(args, tnums))
