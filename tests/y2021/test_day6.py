from aoc.y2021.day6 import clean_input, part1, part2
from aocd.models import Puzzle

test_input = """3,4,3,1,2"""

data = clean_input(test_input)
actual_data = clean_input(Puzzle(2021, 6).input_data)


def test_clean_input():
    assert data == [0, 1, 1, 2, 1, 0, 0, 0, 0]
    assert actual_data[:6] == [0, 129, 42, 44, 45, 40]


def test_part1():
    assert part1(data, days=18) == 26
    assert part1(data) == 5934
    assert part1(actual_data) == 366057


def test_part2():
    assert part2(data) == 26984457539
    assert part2(actual_data) == 1653559299811
