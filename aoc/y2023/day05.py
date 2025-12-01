"""
AOC 2023, Day 5
"""

import re
from typing import Iterable
from functools import reduce


def clean_data(input: str) -> tuple[list[int], list[list[tuple[range, int]]]]:
    seeds, *maps = input.split("\n\n")
    seeds = [*map(int, seeds.split()[1:])]

    traverse = []
    reverse = []
    for i in maps:
        t_sub_rule: list[tuple[range, int]] = []
        r_sub_rule: list[tuple[range, int]] = []
        for t, s, diff in re.findall(r"(\d+) (\d+) (\d+)", i):
            t, s, diff = int(t), int(s), int(diff)
            t_sub_rule.append((range(s, s + diff), t - s))
            r_sub_rule.append((range(t, t + diff), s - t))
        traverse.append(tuple(t_sub_rule))
        reverse.append(tuple(r_sub_rule))

    return seeds, tuple(traverse), tuple(reverse[::-1])


def traverse(seed: int, rules: list[tuple[range, int]]) -> int:
    for range, change in rules:
        if seed in range:
            return seed + change
    return seed


def part1(seeds: Iterable, all_rules: list[list[tuple[range, int]]]):
    return min(reduce(traverse, all_rules, seed) for seed in seeds)


def part2(seeds, all_rules: list[list[tuple[range, int]]]):
    seed_ranges = [*zip(seeds[::2], seeds[1::2])]
    seed_ranges = [range(a, a + b) for a, b in seed_ranges]
    location = 0
    while True:
        seed = reduce(traverse, all_rules, location)
        for r in seed_ranges:
            if seed in r:
                return location
        location += 1


if __name__ == "__main__":
    from aocd.models import Puzzle

    # Get puzzle details and set up input
    puzzle = Puzzle(year=2023, day=5)

    seeds, rules, reverse_rules = clean_data(puzzle.input_data)

    # Submitting answers
    puzzle.answer_a = part1(seeds, rules)
    puzzle.answer_b = part2(seeds, reverse_rules)
