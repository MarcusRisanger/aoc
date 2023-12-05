from aoc.y2020.day2 import parts
from aocd.models import Puzzle

test_input = """1-3 a: abcde
1-3 b: cdefg
2-9 c: ccccccccc"""

actual_data = Puzzle(2020, 2).input_data


def test_parts():
    assert parts(test_input) == (2, 1)
    assert parts(actual_data) == (456, 308)
