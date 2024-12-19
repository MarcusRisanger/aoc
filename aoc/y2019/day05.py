from collections.abc import MutableSequence, Sequence

Instruction = int


def clean_input(inp: str) -> list[Instruction]:
    inst = [*map(int, inp.split(","))]
    return inst


def parse_modes(n: int):
    return n % 100, (n // 100) % 10, (n // 1000)


def get_params(i: int, instructions: Sequence[Instruction]) -> Sequence[Instruction]:
    """Get next instructions, up to 3."""
    return instructions[i + 1 : i + 4]


def get_values(modes: Sequence[int], inst: Sequence[int], instructions: Sequence[Instruction]) -> tuple[int, ...]:
    return tuple(i if m else instructions[i] for m, i in zip(modes, inst))


assert get_values((0, 1), (2, 2), (5, 6, 7, 8)) == (7, 2)
assert get_values((0, 0), (2, 2), (5, 6, 7, 8)) == (7, 7)


def intcode(instructions: MutableSequence[Instruction], inp: int = 0) -> Instruction:
    instructions = instructions[:]
    i = 0  # Start at beginning
    out = 0  # Placeholder output value
    while True:
        code = instructions[i]

        if code == 99 or code % 100 == 99:
            return out

        op, mode1, mode2 = parse_modes(code)
        op_instructions = instructions[i + 1 : i + 4]

        if op in (3, 4):
            address, *_ = op_instructions  # No guarantees that op_instructions has more than 1 element!
        else:
            (_, _, to) = op_instructions
            (param1, param2) = get_values((mode1, mode2), op_instructions, instructions)

        match op:
            case 1:
                instructions[to] = param1 + param2
                i += 4

            case 2:
                instructions[to] = param1 * param2
                i += 4

            case 3:
                instructions[address] = inp
                i += 2

            case 4:
                out = instructions[address]
                i += 2

            case 5:
                i = param2 if param1 != 0 else i + 3

            case 6:
                i = param2 if param1 == 0 else i + 3

            case 7:
                instructions[to] = 1 if param1 < param2 else 0
                i += 4

            case 8:
                instructions[to] = 1 if param1 == param2 else 0
                i += 4


def part1(inst: list[Instruction]) -> str:
    return str(intcode(inst, inp=1))


def part2(inst: list[Instruction]) -> str:
    return str(intcode(inst, inp=5))


if __name__ == "__main__":
    from aocd.models import Puzzle

    # Get puzzle details and set up input
    puzzle = Puzzle(year=2019, day=5)

    instructions = clean_input(puzzle.input_data)
    # Submit answers
    puzzle.answer_a = part1(instructions)
    puzzle.answer_b = part2(instructions)
