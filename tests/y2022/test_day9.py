from aoc.y2022.day9 import SNEK, touching, move_head, move_tail
from aocd.models import Puzzle


test_input_1 = """R 4
U 4
L 3
D 1
R 4
D 1
L 5
R 2"""

test_input_2 = """R 5
U 8
L 8
D 3
R 17
D 10
L 25
U 20"""

actual_data = Puzzle(2022, 9).input_data


def test_touching():
    assert touching(0, 0, 0, 0) == True
    assert touching(0, 1, 0, 0) == True
    assert touching(-1, -1, 0, 0) == True
    assert touching(0, 1, 0, 1) == True
    assert touching(1, 1, 0, 0) == True
    assert touching(0, 0, 1, 1) == True
    assert touching(0, 1, 1, 0) == True
    assert touching(1, -1, 0, 0) == True
    assert touching(2, -1, 0, 0) == False
    assert touching(-2, 1, 0, 0) == False
    assert touching(0, 0, -2, 1) == False
    assert touching(0, 0, 2, -1) == False
    assert touching(2, 0, 0, 1) == False
    assert touching(-2, 0, 0, 1) == False


def test_move_head():
    assert move_head(0, 0, "D") == (1, 0)
    assert move_head(0, 0, "U") == (-1, 0)
    assert move_head(0, 0, "R") == (0, 1)
    assert move_head(0, 0, "L") == (0, -1)


def test_move_tail():
    assert move_tail(2, 1, 0, 0) == (1, 1)
    assert move_tail(2, -1, 0, 0) == (1, -1)
    assert move_tail(1, 1, 0, 0) == (0, 0)
    assert move_tail(-2, 1, 0, 0) == (-1, 1)
    assert move_tail(0, 0, -2, 1) == (-1, 0)


def test_SNEK():
    assert SNEK(test_input_1, 2) == 13
    assert SNEK(test_input_2, 2) == 88
    assert SNEK(actual_data, 2) == 6087
    assert SNEK(test_input_1, 10) == 1
    assert SNEK(test_input_2, 10) == 36
    assert SNEK(actual_data, 10) == 2493
