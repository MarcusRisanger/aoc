from aoc.y2021.day11 import clean_input, octopi_flashes
from aocd.models import Puzzle


test_input = """5483143223
2745854711
5264556173
6141336146
6357385478
4167524645
2176841721
6882881134
4846848554
5283751526"""

data = clean_input(test_input)
actual_input = clean_input(Puzzle(2021, 11).input_data)


def test_clean_input():
    assert data[(0, 2)] == 8
    assert data[(4, 3)] == 7
    assert actual_input[(0, 2)] == 6
    assert actual_input[(4, 3)] == 4


def test_octopi():
    assert octopi_flashes(data) == (1656, 195)
    assert octopi_flashes(actual_input) == (1627, 329)
