from aoc.y2020.day4 import clean_input, part1, part2
from aocd.models import Puzzle

test_input = """ecl:gry pid:860033327 eyr:2020 hcl:#fffffd
byr:1937 iyr:2017 cid:147 hgt:183cm

iyr:2013 ecl:amb cid:350 eyr:2023 pid:028048884
hcl:#cfa07d byr:1929

hcl:#ae17e1 iyr:2013
eyr:2024
ecl:brn pid:760753108 byr:1931
hgt:179cm

hcl:#cfa07d eyr:2025 pid:166559648
iyr:2011 ecl:brn hgt:59in"""

test_data = clean_input(test_input)
actual_data = clean_input(Puzzle(2020, 4).input_data)


def test_clean_input():
    data = clean_input(test_input)
    assert data[:2] == [
        "ecl:gry pid:860033327 eyr:2020 hcl:#fffffd\nbyr:1937 iyr:2017 cid:147 hgt:183cm",
        "iyr:2013 ecl:amb cid:350 eyr:2023 pid:028048884\nhcl:#cfa07d byr:1929",
    ]


def test_part1():
    assert part1(test_data) == 2
    assert part1(actual_data) == 247


def test_part2():
    assert part2(test_data) == 2
    assert part2(actual_data) == 145
