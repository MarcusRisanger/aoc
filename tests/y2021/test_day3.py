from aoc.y2021.day3 import clean_input, count, part1, part2

test_input = """00100
11110
10110
10111
10101
01111
00111
11100
10000
11001
00010
01010"""

data = clean_input(test_input)


def test_clean_input():
    assert data[:2] == ["00100", "11110"]


def test_count():
    assert count(data) == [0, 1, 0, 0, 1]


def test_part1():
    assert part1(data) == 198


def test_part2():
    assert part2(data) == 230
