from aoc.y2022.day1 import clean_input, part1, part2

test_input = """1000
2000
3000

4000

5000
6000

7000
8000
9000

10000"""

data = clean_input(test_input)


def test_day1_part1():
    assert part1(data) == 24000


def test_day1_part2():
    assert part2(data) == 45000
