from aoc.y2020.day1 import clean_input, part1, part2
from aocd.models import Puzzle

test_input = """1721
979
366
299
675
1456"""

data = clean_input(test_input)
actual_data = clean_input(Puzzle(2020, 1).input_data)


def test_clean_input():
    assert data[:3] == [1721, 979, 366]


def test_part1():
    assert part1(data) == 514579
    assert part1(actual_data) == 252724


def test_part2():
    assert part2(data) == 241861950
    assert part2(actual_data) == 276912720
