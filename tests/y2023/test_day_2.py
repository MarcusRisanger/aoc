from aoc.y2023.day2 import clean_input, part1, part2
from aocd.models import Puzzle


test_input = """Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green
Game 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue
Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red
Game 4: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red
Game 5: 6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green"""


data = clean_input(test_input)
actual_data = clean_input(Puzzle(2023, 2).input_data)


def test_clean_input():
    assert data == test_input.splitlines()


def test_part1():
    assert part1(data) == 8
    assert part1(actual_data) == 2156


def test_part2():
    assert part2(data) == 2286
    assert part2(actual_data) == 66909
