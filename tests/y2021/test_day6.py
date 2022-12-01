from aoc.y2021.day6 import clean_input, part1, part2


test_input = """3,4,3,1,2"""


def test_clean_input():
    assert clean_input(test_input) == [0, 1, 1, 2, 1, 0, 0, 0, 0]


def test_part1():
    assert part1(clean_input(test_input), days=18) == 26
    assert part1(clean_input(test_input)) == 5934


def test_part2():
    assert part2(clean_input(test_input)) == 26984457539
