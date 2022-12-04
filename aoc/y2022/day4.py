def clean_input(input_data: str):
    return [
        list(map(int, s.replace("-", ",").split(","))) for s in input_data.splitlines()
    ]


def part1(input_data):
    """Returns number of instruction pairs where one completely covers the other."""
    nums = 0
    for a1, a2, b1, b2 in input_data:
        a, b = set(range(a1, a2 + 1)), set(range(b1, b2 + 1))
        if max([len(a), len(b)]) == len(a | b):
            nums += 1
    return nums


def part2(input_data):
    """Returns number of instruction pairs with any overlap."""
    nums = 0
    for a1, a2, b1, b2 in input_data:
        a, b = set(range(a1, a2 + 1)), set(range(b1, b2 + 1))
        if len(a & b) > 0:
            nums += 1
    return nums


if __name__ == "__main__":
    from aocd.models import Puzzle

    # Get puzzle details and set up input
    puzzle = Puzzle(year=2022, day=4)
    input_data = clean_input(puzzle.input_data)

    # Submit answers
    puzzle.answer_a = part1(input_data)
    puzzle.answer_b = part2(input_data)
