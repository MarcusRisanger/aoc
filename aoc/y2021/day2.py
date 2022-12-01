def clean_input(input_data: str) -> list[tuple[str, int]]:
    return [(comm.split()[0], int(comm.split()[1])) for comm in input_data.splitlines()]


def part1(instructions: list[tuple[str, int]]) -> int:
    """With the given instructions, what is the product of
    final depth and horizontal distance from start?"""
    horizontal, depth = 0, 0
    for command, value in instructions:
        if command == "forward":
            horizontal += value
        elif command == "down":
            depth += value
        elif command == "up":
            depth -= value
    return horizontal * depth


def part2(instructions: list[tuple[str, int]]) -> int:
    """With the given instructions, what is the product of
    final depth and horizontal distance from start?"""
    horizontal, depth, aim = 0, 0, 0
    for command, value in instructions:
        if command == "forward":
            horizontal += value
            depth += value * aim
        elif command == "down":
            aim += value
        elif command == "up":
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
