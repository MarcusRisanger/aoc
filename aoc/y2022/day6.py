import re


def part1(input_data: str) -> int:
    """Returns number of instruction pairs where one completely covers the other."""
    return re.search(r"(\w)(?!\1)(\w)(?!\1|\2)(\w)(?!\1|\2|\3)(\w)", input_data).end()


def part2(input_data: str) -> int:
    length = 14
    for i in range(len(input_data)):
        if len(set(input_data[i : i + length])) == length:
            return i + length


# def part2(input_data: list[list[int]]) -> int:
#     """Returns number of instruction pairs with any overlap."""
#     return sum(map(lambda i: process_line(i, True), input_data))


if __name__ == "__main__":
    from aocd.models import Puzzle

    # Get puzzle details and set up input
    puzzle = Puzzle(year=2022, day=6)

    # Submit answers
    puzzle.answer_a = part1(puzzle.input_data)
    puzzle.answer_b = part2(puzzle.input_data)
