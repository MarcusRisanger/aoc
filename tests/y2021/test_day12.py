from aoc.y2021.day12 import clean_input, walk_graph
from aocd.models import Puzzle


short_test_input = """start-A
start-b
A-c
A-b
b-d
A-end
b-end"""

slightly_longer_test_input = """dc-end
HN-start
start-kj
dc-start
dc-HN
LN-dc
HN-end
kj-sa
kj-HN
kj-dc"""

even_larger_test_input = """fs-end
he-DX
fs-he
start-DX
pj-DX
end-zg
zg-sl
zg-pj
pj-he
RW-he
fs-DX
pj-RW
zg-RW
start-pj
he-WI
zg-he
pj-fs
start-RW"""

test_data_short = clean_input(short_test_input)
test_data_slightly_longer = clean_input(slightly_longer_test_input)
test_data_even_larger = clean_input(even_larger_test_input)
actual_input = clean_input(Puzzle(2021, 12).input_data)


def test_clean_input():
    assert test_data_short["start"] == {"A", "b"}
    assert test_data_short["A"] == {"start", "end", "c", "b"}
    assert test_data_slightly_longer["start"] == {"HN", "dc", "kj"}
    assert test_data_slightly_longer["LN"] == {"dc"}
    assert test_data_even_larger["start"] == {"DX", "RW", "pj"}
    assert test_data_even_larger["fs"] == {"DX", "end", "he", "pj"}


def test_walk_graph():
    assert walk_graph(test_data_short, one_visit=True) == 10
    assert walk_graph(test_data_short, one_visit=False) == 36
    assert walk_graph(test_data_slightly_longer, one_visit=True) == 19
    assert walk_graph(test_data_slightly_longer, one_visit=False) == 103
    assert walk_graph(test_data_even_larger, one_visit=True) == 226
    assert walk_graph(test_data_even_larger, one_visit=False) == 3509
    assert walk_graph(actual_input, one_visit=True) == 4413
    assert walk_graph(actual_input, one_visit=False) == 118803
