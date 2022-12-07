from aoc.y2021.day9 import clean_input, part1, part2
from aocd.models import Puzzle


test_input = """2199943210
3987894921
9856789892
8767896789
9899965678"""

data = clean_input(test_input)
actual_data = clean_input(Puzzle(2021, 9).input_data)
troughs = part1(data)[1]
actual_troughs = part1(actual_data)[1]


def test_clean_input():
    assert data.R == 5
    assert data.C == 10
    assert data.g[0] == [2, 1, 9, 9, 9, 4, 3, 2, 1, 0]
    assert data.g[2] == [9, 8, 5, 6, 7, 8, 9, 8, 9, 2]


def test_part1():
    assert part1(data)[0] == 15
    assert part1(actual_data)[0] == 594


def test_part2():
    assert part2(data, troughs) == 1134
    assert part2(actual_data, actual_troughs) == 858494
