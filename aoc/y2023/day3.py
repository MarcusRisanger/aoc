"""
AOC 2023, Day 3
"""
import math
import re


def parts(data: str):
    data = data.splitlines()
    rows, cols = len(data), len(data[0])

    # Isolate symbols
    sym = {(r, c): [] for r in range(rows) for c in range(cols) if data[r][c] not in "1234567890."}
    part1 = 0
    # Find all numbers for each line
    for r, line in enumerate(data):
        for n in re.finditer(r"(\d+)", line):
            # Define mask of adjacency
            mask = {(r, c) for r in (r, r - 1, r + 1) for c in range(n.start() - 1, n.end() + 1)}

            # Find intersection between mask and symbols
            hits = mask & sym.keys()

            if hits:
                # For part 1, add to the total value
                val = int(n.group())
                part1 += val

                # For part 2, append the value
                # if the symbol is a star
                for hit in hits:
                    if sym[hit] == "*":
                        sym[hit].append(val)

    part2 = sum(math.prod(v) for v in sym.values() if len(v) == 2)

    return part1, part2


if __name__ == "__main__":
    from aocd.models import Puzzle

    # Get puzzle details and set up input
    puzzle = Puzzle(year=2023, day=3)

    ans_a, ans_b = parts(puzzle.input_data)
    # Submit answers
    puzzle.answer_a = ans_a
    puzzle.answer_b = ans_b
