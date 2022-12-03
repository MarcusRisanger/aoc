from aoc.y2022.day13 import process_row, part1, part2
from aocd.models import Puzzle

test_data = """[1,1,3,1,1]
[1,1,5,1,1]

[[1],[2,3,4]]
[[1],4]

[9]
[[8,7,6]]

[[4,4],4,4]
[[4,4],4,4,4]

[7,7,7,7]
[7,7,7]

[]
[3]

[[[]]]
[[]]

[1,[2,[3,[4,[5,6,7]]]],8,9]
[1,[2,[3,[4,[5,6,0]]]],8,9]""".split(
    "\n\n"
)

actual_data = Puzzle(2022, 13).input_data.split("\n\n")


def test_process_row():
    assert process_row(2, 3) == 1
    assert process_row(3, [2, 1, 2]) == -1
    assert process_row([2, 3, 4], [2, 3]) == -1
    assert process_row([[]], []) == -1


def test_part1():
    assert part1(test_data) == 13
    assert part1(actual_data) == 5003


def test_part2():
    assert part2(test_data) == 140
    assert part2(actual_data) == 20280
