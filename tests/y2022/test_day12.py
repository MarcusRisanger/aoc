from aoc.y2022.day12 import clean_input, climb, find_scenic_climb
from aocd.models import Puzzle

test_data = """Sabqponm
abcryxxl
accszExk
acctuvwj
abdefghi"""


test_input = clean_input(test_data)
actual_data = clean_input(Puzzle(2022, 12).input_data)


def test_climb():
    assert climb(*test_input[:-1]) == 31
    assert climb(*actual_data[:-1]) == 420


def test_find_scenic():
    assert find_scenic_climb(*test_input) == 29
    assert find_scenic_climb(*actual_data) == 414
