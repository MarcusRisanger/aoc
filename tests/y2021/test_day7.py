from aoc.y2021.day7 import clean_input, part1, part2


test_input = """16,1,2,0,4,2,7,1,2,14"""


def test_clean_input():
    assert clean_input(test_input)[:3] == [16, 1, 2]


def test_part1():
    assert part1(clean_input(test_input)) == 37


def test_part2():
    assert part2(clean_input(test_input)) == 168
