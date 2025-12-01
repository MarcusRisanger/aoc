from collections.abc import Iterable
from re import findall
from collections import defaultdict
from itertools import product

Mask = str
Value = str
Address = str
MemoryAddress = tuple[Address, Value]
Instruction = tuple[str, Mask] | MemoryAddress


def clean_input(inp: str) -> list[Instruction]:
    """
    Cleans input to rows of:
    - ("mask", "XX01")
    - (")
    """

    def parse_row(row: str) -> Instruction:
        a, b = row.split(" = ")
        if a == "mask":
            return ("mask", b)
        return tuple(findall("[0-9]+", row))  # type: ignore

    return list(parse_row(row) for row in inp.splitlines())


def bin36(i: str | int) -> Value:
    """
    Convert integer to binary string with 36 bits.
    `:b` converts to binary
    """
    return f"{int(i):b}".zfill(36)


def initializer_masking(mask: Mask, value: Value) -> Value:
    """Applies mask to value for initializer."""
    return "".join([m if m in "01" else v for m, v in zip(mask, bin36(value))])


def decoder_addresses(mask: Mask, value: Value) -> list[str]:
    """Retrieves memory addresses for a mask and encoding in"""
    encoded = bin36(value)
    sequence = "".join(e if m == "0" else m if m == "1" else "{}" for m, e in zip(mask, encoded))
    combinations = product("01", repeat=sequence.count("{"))
    return [str(int(sequence.format(*prods), base=2)) for prods in combinations]


def part1(instructions: Iterable[Instruction]) -> str:
    mask = bin36(0)
    memory: dict[Address, int] = defaultdict(int)
    for a, b in instructions:
        if a == "mask":
            mask = b
        else:
            memory[a] = int(initializer_masking(mask, b), base=2)
    return str(sum(memory.values()))


def part2(instructions: Iterable[Instruction]) -> str:
    mask = bin36(0)
    memory: dict[Address, int] = defaultdict(int)
    for a, b in instructions:
        if a == "mask":
            mask = b
        else:
            for i in decoder_addresses(mask, a):
                memory[i] = int(b)
    return str(sum(memory.values()))


if __name__ == "__main__":
    from aocd.models import Puzzle

    puzzle = Puzzle(2020, 14)

    instructions = clean_input(puzzle.input_data)

    puzzle.answer_a = part1(instructions)
    puzzle.answer_b = part2(instructions)
