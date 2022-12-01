"""
AOC 2021 Day 1: 
  - Part 1: Evaluating contiguous list elements
  - Part 2: Evaluating a moving selection of contiguous list elements
"""


def clean_input(input_data: str) -> list[list[int]]:
    return list(map(int, input_data.splitlines()))


def part1(data: list[list[int]]) -> int:
    """How many times does the depth measurement
    increase vs. the previous depth measurement?"""
    return sum(1 for i in range(1, len(data)) if data[i] > data[i - 1])


def part2(data: list[list[int]]) -> int:
    """How many times does the three-measurement sliding window
    depth measure increase vs. the previous three-measurement
    sliding window depth measure?"""
    return sum(
        1
        for i in range(1, len(data))
        if sum(data[i : i + 3]) > sum(data[i - 1 : i + 2])
    )


if __name__ == "__main__":
    from aocd.models import Puzzle

    # Get puzzle details and set up input
    puzzle = Puzzle(year=2021, day=1)
    input_data = clean_input(puzzle.input_data)

    # Submit answers
    puzzle.answer_a = part1(input_data)
    puzzle.answer_b = part2(input_data)
