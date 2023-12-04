"""
AOC 2020, Day 2
"""
import re


def parts(input: str):
    valid_1, valid_2 = 0, 0
    for row in input.splitlines():
        low, high, letter, code = re.findall(r"(\d+).(\d+).(\w+):.(\w+)", row)[0]
        if code.count(letter) >= int(low) and code.count(letter) <= int(high):
            valid_1 += 1
        if (code[int(low) - 1] == letter) ^ (code[int(high) - 1] == letter):
            valid_2 += 1

    return valid_1, valid_2


if __name__ == "__main__":
    from aocd.models import Puzzle

    # Get puzzle details and set up input
    puzzle = Puzzle(year=2020, day=2)

    ans_a, ans_b = parts(puzzle.input_data)
    # Submit answers
    puzzle.answer_a = ans_a
    puzzle.answer_b = ans_b
