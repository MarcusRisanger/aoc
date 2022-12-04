import re


def clean_input(input_data: str) -> list[list[int]]:
    return [list(map(int, re.findall(r"\d+", s))) for s in input_data.splitlines()]


def process_line(line: list[int], part2=False) -> bool:
    a, b, c, d = line
    a, b = set(range(a, b + 1)), set(range(c, d + 1))
    if part2:
        return len(a & b) > 0
    else:
        return max([len(a), len(b)]) == len(a | b)


def part1(input_data: list[list[int]]) -> int:
    """Returns number of instruction pairs where one completely covers the other."""
    return sum(map(process_line, input_data))


def part2(input_data: list[list[int]]) -> int:
    """Returns number of instruction pairs with any overlap."""
    return sum(map(lambda i: process_line(i, True), input_data))


if __name__ == "__main__":
    from aocd.models import Puzzle

    # Get puzzle details and set up input
    puzzle = Puzzle(year=2022, day=4)
    input_data = clean_input(puzzle.input_data)

    # Submit answers
    puzzle.answer_a = part1(input_data)
    puzzle.answer_b = part2(input_data)
