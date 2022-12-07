"""
AOC 2021 Day 2: 
  - Part 1: Applying list-based command instructions using match-case
  - Part 2: Applying more complicated command instructions using match-case
"""


def clean_input(input_data: str) -> list[tuple[str, int]]:
    return [(comm.split()[0], int(comm.split()[1])) for comm in input_data.splitlines()]


def part1(instructions: list[tuple[str, int]]) -> int:
    """With the given instructions, what is the product of
    final depth and horizontal distance from start?"""
    horizontal, depth = 0, 0
    for command, value in instructions:
        match command, value:
            case "forward", value:
                horizontal += value
            case "down", value:
                depth += value
            case "up", value:
                depth -= value
    return horizontal * depth


def part2(instructions: list[tuple[str, int]]) -> int:
    """With the given instructions, what is the product of
    final depth and horizontal distance from start?"""
    horizontal, depth, aim = 0, 0, 0
    for command, value in instructions:
        match command, value:
            case "forward", value:
                horizontal += value
                depth += value * aim
            case "down", value:
                aim += value
            case "up", value:
                aim -= value
    return horizontal * depth


if __name__ == "__main__":
    from aocd.models import Puzzle

    # Get puzzle details and set up input
    puzzle = Puzzle(year=2021, day=2)
    input_data = clean_input(puzzle.input_data)

    # Submit answers
    puzzle.answer_a = part1(input_data)
    puzzle.answer_b = part2(input_data)
