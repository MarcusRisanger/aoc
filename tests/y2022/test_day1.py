from aoc.y2022.day1 import clean_input, part1, part2
from aocd.models import Puzzle

test_input = """1000
2000
3000

4000

5000
6000

7000
8000
9000

10000"""

data = clean_input(test_input)
actual_data = clean_input(Puzzle(2022, 1).input_data)


def test_clean_input():
    assert data[:3] == [6000, 4000, 11000]


def test_part1():
    assert part1(data) == 24000
    assert part1(actual_data) == 72070


def test_part2():
    assert part2(data) == 45000
    assert part2(actual_data) == 211805
