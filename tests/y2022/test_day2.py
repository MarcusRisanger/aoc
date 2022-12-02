from aoc.y2022.day2 import clean_input, points, part1, part2
from aocd.models import Puzzle

test_input = """A Y
B X
C Z"""

data = clean_input(test_input)
actual_data = clean_input(Puzzle(2022, 2).input_data)


def test_clean_input():
    assert data == [("A", "Y"), ("B", "X"), ("C", "Z")]


def test_points():
    assert points("A", "Y") == 8
    assert points("B", "X") == 1
    assert points("C", "Z") == 6


def test_day1_part1():
    assert part1(data) == 15
    assert part1(actual_data) == 9177


def test_day1_part2():
    assert part2(data) == 12
    assert part2(actual_data) == 12111
