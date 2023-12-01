def clean_input(data: str) -> list[list[str]]:
    """Cleans input data using simple splits.
    Splits string into lines."""
    return [[x for x in row if x.isnumeric()] for row in data.splitlines()]


def part1(data: list[list[str]]) -> int:
    """
    Find the sum of the numbers made up by combining the first and
    last digit for each line in the list. Only use digits.
    """
    return sum(int(x[0] + x[-1]) for x in list(filter(len, data)))


def part2(data: list[list[int]]) -> int:
    """
    Take into account also numbers that are written out as text.
    """
    return 1


if __name__ == "__main__":
    from aocd.models import Puzzle

    # Get puzzle details and set up input
    puzzle = Puzzle(year=2023, day=1)
    input_data = clean_input(puzzle.input_data)

    print(input_data[:3])

    # Submit answers
    puzzle.answer_a = part1(input_data)
    # puzzle.answer_b = part2(input_data)
