import itertools
import math
import re


def clean_input(input: str) -> tuple[str, dict[str, dict[str, str]]]:
    key, _, *nodes = input.split("\n")
    graph: dict[str, dict[str, str]] = {
        n: {"L": left, "R": right}
        for n, left, right in [re.findall(r"\w+", n) for n in nodes]
    }

    return key, graph


def part1(key: str, graph: dict[str, dict[str, str]], start="AAA", stop="ZZZ") -> str:  # type: ignore[return]
    for step, i in enumerate(itertools.cycle(key)):
        if start.endswith(stop):
            return str(step)
        start = graph[start][i]


def part2(key: str, graph: dict[str, dict[str, str]]) -> str:
    starts = list(filter(lambda x: x.endswith("A"), graph.keys()))
    return str(math.lcm(*[part1(key, graph, start, "Z") for start in starts]))


if __name__ == "__main__":
    from aocd.models import Puzzle

    # Get puzzle details and set up input
    puzzle = Puzzle(year=2023, day=8)
    input = clean_input(puzzle.input_data)

    # Submitting answers
    puzzle.answer_a = part1(*input)
    puzzle.answer_b = part2(*input)
