from collections import defaultdict
import re


def clean_input(inp: str) -> tuple[list[list[str]], list[list[int]]]:
    crates_raw, instr = inp.split("\n\n")
    gen = [row[1::4] for row in crates_raw.splitlines()]
    crates = defaultdict(list)
    for col, key in enumerate(gen[-1]):
        for row in gen[:-1]:
            if row[col] != " ":
                crates[int(key)].append(row[col])

    return crates, [
        list(map(int, re.findall(r"\d+", row))) for row in instr.splitlines()
    ]


def part1(crates: dict[int, list[str]], instructions: list[list[int]]):
    for m, f, t in instructions:
        crates[t], crates[f] = crates[f][:m][::-1] + crates[t], crates[f][m:]
    return "".join(v[0] for v in crates.values())


def part2(crates: dict[int, list[str]], instructions: list[list[int]]):
    for m, f, t in instructions:
        crates[t], crates[f] = crates[f][:m] + crates[t], crates[f][m:]
    return "".join(v[0] for v in crates.values())


if __name__ == "__main__":
    from aocd.models import Puzzle

    # Get puzzle details and set up input
    puzzle = Puzzle(year=2022, day=5)
    crates, instructions = clean_input(puzzle.input_data)

    # Submit answers
    puzzle.answer_a = part1(crates.copy(), instructions)
    puzzle.answer_b = part2(crates, instructions)
