# Dynamic programming approach
# Great writeup here: https://advent-of-code.xavd.id/writeups/2023/day/12/
from typing import Generator
import re
from itertools import product
from functools import cache


def parse_line(line: str, p2: bool) -> tuple[str, tuple[int, ...]]:
    springs, groups = line.split(" ")
    if p2:
        return "?".join([springs] * 5), tuple(int(g) for g in groups.split(",") * 5)
    return springs, tuple(int(g) for g in groups.split(","))


def transform_input(inp: str, p2: bool = False) -> list[tuple[str, tuple[int, ...]]]:
    return [parse_line(row, p2) for row in inp.splitlines()]


@cache
def valid_solutions(record: str, groups: tuple[int, ...]) -> int:
    """
    Base parts of the problem:
        1) If there is no record, this is OK if there are no groups.
        2) If there are no groups, this is OK if there are no # left.

    After the base parts are solved, we have to recursively break down
    our record and groups to this case.
    """
    if not record:
        # If the record is exhausted, there should be no groups left.
        return len(groups) == 0
    if not groups:
        # If there are no groups left, there should be no "#" left in record.
        return "#" not in record

    char, rest_of_record = record[0], record[1:]

    if char == ".":
        # We can skip the parts where this character is first in record
        return valid_solutions(rest_of_record, groups)

    if char == "#":
        # When we hit a hash, we first grab the first remaining group
        group, rest_of_groups = groups[0], groups[1:]

        # We check for key properties of record and group

        if (
            len(record) >= group  # Record sufficiently long
            and all(c != "." for c in record[:group])  # Record can support group
            and (
                len(record) == group  # Record exactly long enough
                or record[group] != "#"  # Next character not hash (group too big)
            )
        ):
            return valid_solutions(rest_of_record[group:], rest_of_groups)
        return 0  # Invalid

    if char == "?":
        if_mark_is_hash = valid_solutions("#" + rest_of_record, groups)
        if_mark_is_period = valid_solutions("." + rest_of_record, groups)
        return if_mark_is_hash + if_mark_is_period

    return 0  # static type checker complains..


def part1(inp: str) -> int:
    rows = transform_input(inp)
    return sum(valid_solutions(record, groups) for record, groups in rows)


def part2(inp: str) -> int:
    rows = transform_input(inp, p2=True)
    return sum(valid_solutions(record, groups) for record, groups in rows)


if __name__ == "__main__":
    from aocd.models import Puzzle

    # Get puzzle details and set up input
    puzzle = Puzzle(year=2023, day=12)

    # Submitting answers
    puzzle.answer_a = part1(puzzle.input_data)
    puzzle.answer_b = part2(puzzle.input_data)
