from aocd.models import Puzzle
from collections import defaultdict
import re


def clean_input(inp: str) -> tuple[list[list[str]], list[list[int]]]:
    crates_raw, instr = inp.split("\n\n")
    gen = [[i for i in row[1::4]] for row in crates_raw.splitlines()]
    crates = defaultdict(list)
    for col, key in enumerate(gen[-1]):
        for row in gen[:-1]:
            if (element := row[col]) != " ":
                crates[int(key)].append(element)

    return crates, [
        list(map(int, re.findall(r"\d+", row))) for row in instr.splitlines()
    ]


def part1(crates: dict[int, list[str]], instructions: list[list[int]]):
    for move, from_, to in instructions:
        crates[to] = crates[from_][:move][::-1] + crates[to]
        crates[from_] = crates[from_][move:]
    return "".join(v[0] for v in crates.values())


def part2(crates: dict[int, list[str]], instructions: list[list[int]]):
    for move, from_, to in instructions:
        crates[to] = crates[from_][:move] + crates[to]
        crates[from_] = crates[from_][move:]
    return "".join(v[0] for v in crates.values())


if __name__ == "__main__":
    from aocd.models import Puzzle

    # Get puzzle details and set up input
    puzzle = Puzzle(year=2022, day=5)
    crates, instructions = clean_input(puzzle.input_data)

    # Submit answers
    puzzle.answer_a = part1(crates.copy(), instructions)
    puzzle.answer_b = part2(crates, instructions)
