from collections import defaultdict
from collections.abc import Mapping
from functools import cache
from re import findall


@cache
def hash(arg: str) -> int:
    """Hashing function as specified."""
    v = 0
    for letter in arg:
        v += ord(letter)
        v *= 17
        v = v % 256
    return v % 256


def get_instructions(arg: str) -> list[tuple[str, ...]]:
    return findall(r"(?:(\w+)([\=\-])(\d?)),*", arg)


def parse_hashmap(instructions: list[tuple[str, ...]]) -> dict[int, dict[str, int]]:
    """
    Based on the instructions, do as specified in the prompt.
    The prompt states the lense order is important, and Python dicts are ordered
    by insertion by default. Phew!
    """
    # Defaultdict allows creation of keys on assignment
    hashmap: dict[int, dict] = defaultdict(dict)
    for label, instruction, focal_length in instructions:
        val = hash(label)
        if instruction == "-":
            hashmap[val].pop(label, None)  # Default arg suppresses KeyError, nifty
        else:
            hashmap[val][label] = int(focal_length)
    return hashmap


def score_hashmap(hashmap: Mapping[int, Mapping[str, int]]):
    """Get the HASHMAP instructions score."""
    total = 0
    for k, v in hashmap.items():
        if not v:
            continue
        for slot, focal_length in enumerate(v.values(), 1):
            total += (k + 1) * slot * focal_length
    return total


def part1(inp: str) -> str:
    return str(sum(map(hash, inp.split(","))))


def part2(inp: str) -> str:
    hashmap = parse_hashmap(get_instructions(inp))
    return str(score_hashmap(hashmap))


if __name__ == "__main__":
    from aocd.models import Puzzle

    puzzle = Puzzle(2023, 15)

    puzzle.answer_a = part1(puzzle.input_data)
    puzzle.answer_b = part2(puzzle.input_data)
