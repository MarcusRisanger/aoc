from aoc.y2022.day6 import part1, part2
from aocd.models import Puzzle
import pytest

test_input = "zcfzfwzzqfrljwzlrfnpqdbhtmscgvjw"

actual_data = Puzzle(2022, 6).input_data


def test_part1():
    assert part1(test_input) == 11
    assert part1(actual_data) == 1647


def test_part2():
    assert part2(test_input, 14) == 26
    assert part2(actual_data, 14) == 2447
