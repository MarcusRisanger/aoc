from aoc.y2021.day14 import polymer
from aocd.models import Puzzle

test_input = """NNCB

CH -> B
HH -> N
CB -> H
NH -> C
HB -> C
HC -> B
HN -> C
NN -> C
BH -> H
NC -> B
NB -> B
BN -> B
BB -> N
BC -> B
CC -> N
CN -> C"""


def test_polymer():
    assert polymer(test_input) == (1588, 2188189693529)
    assert polymer(Puzzle(2021, 14).input_data) == (2068, 2158894777814)
