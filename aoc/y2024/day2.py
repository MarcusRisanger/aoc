from itertools import combinations
from collections.abc import Sequence

Report = Sequence[int]


def clean_input(inp: str) -> list[Report]:
    """Cleans input to a list of integers."""
    return [[*map(int, row.split())] for row in inp.splitlines()]


def safe(nums: Report) -> bool:
    """Determines if all elements in a report is strictly ascending or descending, in steps of 1-3."""
    return any(all(1 <= a - b <= 3 for a, b in zip(n, n[1:])) for n in [nums, nums[::-1]])


def max_one_unsafe(nums: Report) -> bool:
    """Determines if any of all possible list slice combinations are safe."""
    return safe(nums) or any(safe(ns) for ns in combinations(nums, len(nums) - 1))


def part1(reports: Sequence[Report]) -> int:
    """Checks each report and counts those that are safe."""
    return sum(map(safe, reports))


def part2(reports: Sequence[Report]) -> int:
    """Checks each report and counts those that are safe with max 1 value removed."""
    return sum(map(max_one_unsafe, reports))


if __name__ == "__main__":
    from aocd.models import Puzzle

    # Get puzzle details and set up input
    puzzle = Puzzle(year=2024, day=2)
    input_data = clean_input(puzzle.input_data)

    # Submit answers
    puzzle.answer_a = str(part1(input_data))
    puzzle.answer_b = str(part2(input_data))
