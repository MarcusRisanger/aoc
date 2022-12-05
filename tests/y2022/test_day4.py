from aoc.y2022.day4 import clean_input, part1, part2
from aocd.models import Puzzle

minimal_test_input = """1-2,3-4
1-3,3-10
10-12,9-20"""

test_input = """2-4,6-8
2-3,4-5
5-7,7-9
2-8,3-7
6-6,4-6
2-6,4-8"""

minimal_data = clean_input(minimal_test_input)
data = clean_input(test_input)
actual_data = clean_input(Puzzle(2022, 4).input_data)


def test_clean_input():
    assert minimal_data == [[1, 2, 3, 4], [1, 3, 3, 10], [10, 12, 9, 20]]
    assert data[:2] == [[2, 4, 6, 8], [2, 3, 4, 5]]


def test_part1():
    assert part1(minimal_data) == 1
    assert part1(data) == 2
    assert part1(actual_data) == 550


def test_part2():
    assert part2(minimal_data) == 2
    assert part2(data) == 4
    assert part2(actual_data) == 931
