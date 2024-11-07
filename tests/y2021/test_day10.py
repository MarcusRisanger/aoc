from aoc.y2021.day10 import syntax_error_score
from aocd.models import Puzzle


test_input = """[({(<(())[]>[[{[]{<()<>>
[(()[<>])]({[<{<<[]>>(
{([(<{}[<>[]}>{[]{[(<()>
(((({<>}<{<{<>}{[]{[]{}
[[<[([]))<([[{}[[()]]]
[{[{({}]{}}([{[{{{}}([]
{<[[]]>}<{[{[{[]{()[[[]
[<(<(<(<{}))><([]([]()
<{([([[(<>()){}]>(<<{{
<{([{{}}[<[[[<>{}]]]>[]]"""

actual_input = Puzzle(2021, 10).input_data


def test_syntax_error_score():
    assert syntax_error_score(test_input) == (26397, 288957)
    assert syntax_error_score(actual_input) == (299793, 3654963618)
