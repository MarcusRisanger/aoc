from aoc.y2023.day1 import clean_input, part1, part2
from aocd.models import Puzzle


test_input_p1 = """1abc2
pqr3stu8vwx
a1b2c3d4e5f
treb7uchet"""

test_input_p2 = """two1nine
eightwothree
abcone2threexyz
xtwone3four
4nineeightseven2
zoneight234
7pqrstsixteen"""


data_p1 = clean_input(test_input_p1)
data_p2 = clean_input(test_input_p2)
actual_data = clean_input(Puzzle(2023, 1).input_data)


def test_clean_input():
    assert data_p2[:3] == ["two1nine", "eightwothree", "abcone2threexyz"]


def test_part1():
    assert part1(data_p1) == 142
    assert part1(actual_data) == 53651


def test_part2():
    assert part2(data_p2) == 281
    assert part2(actual_data) == 53894
