from aoc.y2021.day5 import clean_input, part1, part2


test_input = """0,9 -> 5,9
8,0 -> 0,8
9,4 -> 3,4
2,2 -> 2,1
7,0 -> 7,4
6,4 -> 2,0
0,9 -> 2,9
3,4 -> 1,4
0,0 -> 8,8
5,5 -> 8,2"""


def test_clean_input():
    assert clean_input(test_input)[:2] == [[0, 9, 5, 9], [8, 0, 0, 8]]


def test_part1():
    coordinates = clean_input(test_input)

    assert part1(coordinates) == 5


def test_part2():
    coordinates = clean_input(test_input)

    assert part2(coordinates) == 12
