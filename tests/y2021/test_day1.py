from aoc.y2020.day1 import clean_input, part1, part2
from aocd.models import Puzzle

test_input = """"""

data = clean_input(test_input)
actual_data = clean_input(Puzzle(2021, 1).input_data)


def test_clean_input():
    assert data[:3] == [199, 200, 208]


def test_part1():
    assert part1(data) == 7
    assert part1(actual_data) == 1655


def test_part2():
    assert part2(data) == 5
    assert part2(actual_data) == 1683
