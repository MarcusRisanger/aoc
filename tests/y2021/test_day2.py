from aoc.y2021.day2 import clean_input, part1, part2

test_input = """forward 5
down 5
forward 8
up 3
down 8
forward 2"""

data = clean_input(test_input)


def test_clean_input():
    assert data[:3] == [("forward", 5), ("down", 5), ("forward", 8)]


def test_part1():
    assert part1(data) == 150


def test_part2():
    assert part2(data) == 900
