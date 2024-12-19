from collections.abc import MutableSequence
from itertools import product

Instruction = int


def clean_input(inp: str) -> list[Instruction]:
    inst = [*map(int, inp.split(","))]
    return inst


def injector(inst: list[Instruction], noun: Instruction, verb: Instruction) -> int:
    inst = inst.copy()
    inst[1], inst[2] = noun, verb
    return intcode(inst)


def intcode(instructions: MutableSequence[Instruction]) -> Instruction:
    i = 0
    while True:
        op, inp1, inp2, to = instructions[i : i + 4]
        match op:
            case 99:
                return instructions[0]
            case 1:
                instructions[to] = instructions[inp1] + instructions[inp2]
            case 2:
                instructions[to] = instructions[inp1] * instructions[inp2]
        i += 4


def part1(inst: list[Instruction]) -> str:
    return str(injector(inst, 12, 2))


def part2(inst: list[Instruction]) -> str:  # type: ignore[return]
    for noun, verb in product(range(100), repeat=2):
        if injector(inst, noun, verb) == 19690720:
            return str(100 * noun + verb)


if __name__ == "__main__":
    from aocd.models import Puzzle

    # Get puzzle details and set up input
    puzzle = Puzzle(year=2019, day=2)

    instructions = clean_input(puzzle.input_data)

    # Submit answers
    puzzle.answer_a = part1(instructions)
    puzzle.answer_b = part2(instructions)
