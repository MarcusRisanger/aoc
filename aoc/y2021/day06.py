"""
AOC 2021, Day 6:
  - Part 1 and 2: Keeping track of fish ages and fish spawns!
"""


def clean_input(input_data: str) -> list[int]:
    fish = [0] * 9
    for i in input_data.split(","):
        fish[int(i)] += 1
    return fish


def lanternfish(fish: list[int], days: int) -> int:
    for i in range(days):
        fish = fish[1:] + [fish[0]]
        fish[6] += fish[-1]
    return sum(fish)


def part1(fish: list[int], days: int = 80) -> int:
    return lanternfish(fish, days)


def part2(fish: list[int]) -> int:
    return lanternfish(fish, 256)


if __name__ == "__main__":
    from aocd.models import Puzzle

    # Get puzzle details and set up input
    puzzle = Puzzle(year=2021, day=6)
    fish = clean_input(puzzle.input_data)

    puzzle.answer_a = part1(fish)
    puzzle.answer_b = part2(fish)
