from aoc.y2022.day5 import clean_input, part1, part2
from aocd.models import Puzzle


test_input = """    [D]    
[N] [C]    
[Z] [M] [P]
 1   2   3 

move 1 from 2 to 1
move 3 from 1 to 3
move 2 from 2 to 1
move 1 from 1 to 2"""

data = clean_input(test_input)
actual_data = clean_input(Puzzle(2022, 5).input_data)


def test_clean_input():
    assert data[0][1] == ["N", "Z"]
    assert data[1][1] == [3, 1, 3]


def test_part1():
    assert part1(data[0].copy(), data[1]) == "CMZ"
    assert part1(actual_data[0].copy(), actual_data[1]) == "FWSHSPJWM"


def test_part2():
    assert part2(*data) == "MCD"
    assert part2(*actual_data) == "PWPWHGFZS"
