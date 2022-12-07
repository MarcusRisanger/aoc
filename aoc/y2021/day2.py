"""
AOC 2021 Day 2: 
  - Part 1: Applying list-based command instructions using match-case
  - Part 2: Applying more complicated command instructions using match-case
"""


def clean_input(input_data: str) -> list[tuple[str, int]]:
    return [(comm.split()[0], int(comm.split()[1])) for comm in input_data.splitlines()]


def part1(input_data: str) -> int:
    """With the given instructions, what is the product of
    final depth and horizontal distance from start?"""
    horizontal, depth = 0, 0
    for row in input_data.splitlines():
        match row.split():
            case "forward", value:
                horizontal += int(value)
            case "down", value:
                depth += int(value)
            case "up", value:
                depth -= int(value)
    return horizontal * depth


def part2(input_data: str) -> int:
    """With the given instructions, what is the product of
    final depth and horizontal distance from start?"""
    horizontal, depth, aim = 0, 0, 0
    for row in input_data.splitlines():
        match row.split():
            case "forward", value:
                horizontal += int(value)
                depth += int(value) * aim
            case "down", value:
                aim += int(value)
            case "up", value:
                aim -= int(value)
    return horizontal * depth


if __name__ == "__main__":
    from aocd.models import Puzzle

    # Get puzzle details and set up input
    puzzle = Puzzle(year=2021, day=2)

    # Submit answers
    puzzle.answer_a = part1(puzzle.input_data)
    puzzle.answer_b = part2(puzzle.input_data)
