from aoc.y2021.day13 import clean_input, fold_origami
from aocd.models import Puzzle

test_data = """6,10
0,14
9,10
0,3
10,4
4,11
6,0
6,12
4,1
0,13
10,12
3,4
3,0
8,4
1,10
2,14
8,10
9,0

fold along y=7
fold along x=5"""


test_data = clean_input(test_data)
actual_input = clean_input(Puzzle(2021, 13).input_data)


def test_clean_input():
    assert test_data[1] == [("y", 7), ("x", 5)]
    assert test_data[0][0, 0] == 0
    assert test_data[0][10, 6] == 1
    assert actual_input[1][:2] == [("x", 655), ("y", 447)]
    assert actual_input[0][257, 47] == 1
    assert actual_input[0][257, 0] == 0


def test_fold_origamin():
    assert fold_origami(*test_data) == 17
    assert fold_origami(*actual_input) == 775
