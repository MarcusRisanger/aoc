from aoc.y2021.day7 import clean_input, part1, part2
from aocd.models import Puzzle

test_input = """16,1,2,0,4,2,7,1,2,14"""

data = clean_input(test_input)
actual_data = clean_input(Puzzle(2021, 7).input_data)


def test_clean_input():
    assert data[:3] == [16, 1, 2]


def test_part1():
    assert part1(data) == 37
    assert part1(actual_data) == 336040


def test_part2():
    assert part2(data) == 168
    assert part2(actual_data) == 94813675
