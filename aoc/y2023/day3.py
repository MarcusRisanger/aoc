"""
AOC 2023, Day 3
"""
from collections import defaultdict
import math
import re


def clean_input(input: str) -> tuple[dict[complex, str], str, str]:
    data = input.splitlines()

    j_max = len(data)
    i_max = len(data[0])

    out = dict()
    for j, row in enumerate(data):
        for i, val in enumerate(row):
            out[complex(i, j)] = val
    return out, i_max, j_max


def get_neighbors(_i: list[str], _j: str) -> bool:
    _i, _j = [int(i) for i in _i], int(_j)
    _min, _max = min(_i) - 1, max(_i) + 1
    neighbors = {(i, j) for i in range(_min, _max + 1) for j in (_j + 1, _j - 1)}
    neighbors.update((i, _j) for i in (_min, _max))

    for n in neighbors:
        yield complex(*n)


def part1(schema: dict[complex, str], i_max: int, j_max: int):
    out = 0
    for j in range(j_max):
        i_s, add = list(), ""
        for i in range(i_max):
            val = schema.get(complex(i, j))
            if val.isnumeric():
                add += val
                i_s.append(i)
            if (not val.isnumeric() or i == i_max - 1) and i_s:
                if any([schema.get(neigh) != "." for neigh in get_neighbors(i_s, j) if neigh in schema]):
                    out += int("".join(add))
                i_s, add = list(), ""
    return out


def part2(schema: dict[complex, str], i_max: int, j_max: int):
    gears: dict[complex, list[int]] = defaultdict(list)
    for j in range(j_max):
        i_s, add = list(), ""
        for i in range(i_max):
            val = schema.get(complex(i, j))
            if val.isnumeric():
                add += val
                i_s.append(i)
            if (not val.isnumeric() or i == i_max - 1) and i_s:
                data = {neigh for neigh in get_neighbors(i_s, j) if neigh in schema and schema.get(neigh) == "*"}
                for node in data:
                    gears[node].append(int("".join(add)))
                i_s, add = list(), ""
    return sum(math.prod(v) for _, v in gears.items() if len(v) == 2)


if __name__ == "__main__":
    from aocd.models import Puzzle

    # Get puzzle details and set up input
    puzzle = Puzzle(year=2023, day=3)
    input_data = clean_input(puzzle.input_data)

    # Submit answers
    print(part1(*input_data))
    puzzle.answer_a = part1(*input_data)
    puzzle.answer_b = part2(*input_data)
