from aoc.y2022.day3 import clean_input, part1, part2, part1_verbose
from aocd.models import Puzzle

minimal_test_input = """abcABc"""

test_input = """vJrwpWtwJgWrhcsFMMfFFhFp
jqHRNqRjqzjGDLGLrsFMfFZSrLrFZsSL
PmmdzqPrVvPwwTWBwg
wMqvLMZHhHMvwLHjbvcjnnSBnvTQFn
ttgJtRGJQctTZtZT
CrZsJsPPZsGzwwsLwLmpwMDw"""

minimal_data = clean_input(minimal_test_input)
data = clean_input(test_input)
actual_data = clean_input(Puzzle(2022, 3).input_data)


def test_clean_input():
    assert minimal_data == [("abc", "ABc")]
    assert data[:2] == [
        ("vJrwpWtwJgWr", "hcsFMMfFFhFp"),
        ("jqHRNqRjqzjGDLGL", "rsFMfFZSrLrFZsSL"),
    ]


def test_part1():
    assert part1(minimal_data) == 3
    assert part1(data) == 157
    assert part1(actual_data) == 7850


def test_part1_vb():
    assert part1_verbose(minimal_data) == 3
    assert part1_verbose(data) == 157
    assert part1_verbose(actual_data) == 7850


def test_part2():
    assert part2(data) == 70
    assert part2(actual_data) == 2581
