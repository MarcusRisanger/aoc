import numpy as np
from itertools import repeat
from functools import reduce


def eval(row: str, p=1):
    r = np.array(row.split()).astype(int)
    first: list = list()
    last: list = list()
    while True:
        first.insert(0, r[0])
        last.append(r[-1])
        if all(r == 0):
            if p == 1:
                return sum(last)
            return reduce(lambda x, y: y - x, first[1:], 0)
        r = r[1:] - r[:-1]


def part1(input: str) -> str:
    return str(int(sum(map(eval, input.split("\n")))))


def part2(input: str) -> str:
    inp = input.split("\n")
    return str(int(sum(map(eval, inp, repeat(2)))))


if __name__ == "__main__":
    from aocd.models import Puzzle

    # Get puzzle details and set up input
    puzzle = Puzzle(year=2023, day=9)

    # Submitting answers
    puzzle.answer_a = part1(puzzle.input_data)
    puzzle.answer_b = part2(puzzle.input_data)
