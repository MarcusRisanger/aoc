from aoc.y2022.day7 import clean_input, part1, part2
from aocd.models import Puzzle


test_input = """$ cd /
$ ls
dir a
14848514 b.txt
8504156 c.dat
dir d
$ cd a
$ ls
dir e
29116 f
2557 g
62596 h.lst
$ cd e
$ ls
584 i
$ cd ..
$ cd ..
$ cd d
$ ls
4060174 j
8033020 d.log
5626152 d.ext
7214296 k"""

data = clean_input(test_input)
actual_data = clean_input(Puzzle(2022, 7).input_data)


def test_clean_input():
    assert data["/"], data["/a/"] == (48381165, 94853)
    assert actual_data["/gnpd/dwqbhgc/sbnhc/"] == 731541


def test_part1():
    assert part1(data) == 95437
    assert part1(actual_data) == 1428881


def test_part2():
    assert part2(data) == 24933642
    assert part2(actual_data) == 10475598
