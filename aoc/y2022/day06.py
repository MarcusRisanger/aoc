import re


def part1(input_data: str) -> int:
    """Fancy schmancy regex, useless compared to part 2."""
    return re.search(r"(\w)(?!\1)(\w)(?!\1|\2)(\w)(?!\1|\2|\3)(\w)", input_data).end()


def part2(input_data: str, sig_length: int) -> int:
    for i in range(len(input_data)):
        if len(set(input_data[i : i + sig_length])) == sig_length:
            return i + sig_length


if __name__ == "__main__":
    from aocd.models import Puzzle

    # Get puzzle details and set up input
    puzzle = Puzzle(year=2022, day=6)

    # Submit answers
    puzzle.answer_a = part1(puzzle.input_data)
    puzzle.answer_b = part2(puzzle.input_data, 14)
