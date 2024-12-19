"""
AOC 2021, Day 7:
  - Part 1 and 2: Statistics!
"""

from statistics import median, mean


def clean_input(input_data: str) -> list[int]:
    return list(map(int, input_data.split(",")))


def part1(crabs: list[int]) -> int:
    median_ = int(median(crabs))
    return sum(abs(crab - median_) for crab in crabs)


def part2(crabs: list[int]) -> int:
    means = [int(mean(crabs)), int(mean(crabs) + 1)]

    def fuel_cost(steps):
        return sum(range(steps + 1))

    return min([sum(fuel_cost(abs(crab - m)) for crab in crabs) for m in means])


if __name__ == "__main__":
    from aocd.models import Puzzle

    # Get puzzle details and set up input
    puzzle = Puzzle(year=2021, day=7)
    crabs = clean_input(puzzle.input_data)

    puzzle.answer_a = part1(crabs)
    print(part2(crabs))
    puzzle.answer_b = part2(crabs)
