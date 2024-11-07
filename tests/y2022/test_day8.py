from aoc.y2022.day8 import clean_input, evaluate_tree, solve
from aocd.models import Puzzle


test_input = """30373
25512
65332
33549
35390"""

data = clean_input(test_input)
actual_data = clean_input(Puzzle(2022, 8).input_data)


def test_clean_input():
    assert (data.R, data.C) == (4, 4)
    assert (data.g[1][1], data.g[3][1]) == (5, 3)
    assert (actual_data.R, actual_data.C) == (98, 98)


def test_evaluate():
    assert evaluate_tree(data, *(3, 2)) == (True, 8)
    assert evaluate_tree(data, *(1, 2)) == (True, 4)
    assert evaluate_tree(data, *(3, 1)) == (False, 1)


def test_solve():
    assert solve(data) == (21, 8)
    assert solve(actual_data) == (1809, 479400)
