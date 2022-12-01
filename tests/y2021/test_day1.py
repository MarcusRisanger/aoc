from aoc.y2021.day1 import clean_input, part1, part2

test_input = """199
200
208
210
200
207
240
269
260
263"""

data = clean_input(test_input)


def test_part1():
    assert part1(data) == 7


def test_part2():
    assert part2(data) == 5
