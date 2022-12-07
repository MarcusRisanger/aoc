from aoc.y2021.day2 import clean_input, part1, part2
from aocd.models import Puzzle

test_input = """forward 5
down 5
forward 8
up 3
down 8
forward 2"""

actual_data = Puzzle(2021, 2).input_data


def test_part1():
    assert part1(test_input) == 150
    assert part1(actual_data) == 2073315


def test_part2():
    assert part2(test_input) == 900
    assert part2(actual_data) == 1840311528
