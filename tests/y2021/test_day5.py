from aoc.y2021.day5 import clean_input, get_hits, part1, part2
from aocd.models import Puzzle

test_input = """0,9 -> 5,9
8,0 -> 0,8
9,4 -> 3,4
2,2 -> 2,1
7,0 -> 7,4
6,4 -> 2,0
0,9 -> 2,9
3,4 -> 1,4
0,0 -> 8,8
5,5 -> 8,2"""

data = clean_input(test_input)
actual_data = clean_input(Puzzle(2021, 5).input_data)


def test_clean_input():
    assert clean_input(test_input)[:2] == [[0, 9, 5, 9], [8, 0, 0, 8]]
    assert get_hits(*[0, 4]) == [0, 1, 2, 3, 4]
    assert get_hits(*[4, 0]) == [4, 3, 2, 1, 0]


def test_part1():
    assert part1(data) == 5
    assert part1(actual_data) == 5698


def test_part2():
    assert part2(data) == 12
    assert part2(actual_data) == 15463
