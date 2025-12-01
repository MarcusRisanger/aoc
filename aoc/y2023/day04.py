"""
AOC 2023, Day 4
"""


def score(line: str, part: int = 1):
    wins, nums = line.split(": ")[1].split("|")
    winning = set(wins.split(" ")) & set(nums.split(" "))
    if part == 1:
        return 2 ** (len(winning) - 1) if winning else 0
    else:
        return len(winning)


def part1(data: str):
    return sum(map(score, data.splitlines()))


def part2(data: str):
    repeats = {i: 1 for i in range(len(data.splitlines()))}
    for i, line in enumerate(data.splitlines()):
        for j in range(1, score(line, 2) + 1):
            repeats[i + j] += repeats[i]
    return sum(repeats.values())


if __name__ == "__main__":
    from aocd.models import Puzzle

    # Get puzzle details and set up input
    puzzle = Puzzle(year=2023, day=4)

    # Submit answers
    puzzle.answer_a = part1(puzzle.input_data)
    puzzle.answer_b = part2(puzzle.input_data)
