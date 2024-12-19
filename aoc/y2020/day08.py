Instruction = tuple[str, int]
Line = int
Program = dict[Line, Instruction]


def clean_input(inp: str) -> Program:
    """Cleans input by parsing into a dict with line number as key and instruction as value."""

    def parse_instruction(arg: str) -> Instruction:
        op, n = arg.split(" ")
        return (op, int(n))

    return {i: parse_instruction(instr) for i, instr in enumerate(inp.splitlines())}


def swap_op(arg: str) -> str:
    """Swaps operation for `jmp` and `nop`."""
    key = {"jmp": "nop", "nop": "jmp"}
    return key[arg] if arg in key else arg


def run_program(program: Program, override_at: Line = -1) -> tuple[bool, str]:
    """
    Runs the program and terminates upon loop or if the instructions point beyond the program.

    For part 2, this function has an `override_at` parameter that replaces a jmp/acc
    """

    line = acc = 0
    seen: set[Line] = set()

    while True:
        if line >= len(program):
            return True, str(acc)
        if line in seen:
            return False, str(acc)
        seen.add(line)
        op, n = program[line]

        if line == override_at:
            op = swap_op(op)
        if op == "acc":
            acc += n
        if op == "jmp":
            line = line + n - 1  # Offsets below
        line += 1


def part1(program: Program) -> str:
    """Return the accumulation property on the base program instructions."""
    return run_program(program)[1]


def part2(program: Program) -> str:  # type: ignore
    """
    Return the accumulation property for the modified program instructions
    that are able to exit cleanly without looping, by replacing a single
    `jmp` with `nop` or vice versa.
    """
    indeces = (i for i in range(len(program)) if program[i][0] in ("jmp", "nop"))
    for i in indeces:
        terminated, acc = run_program(program, i)
        if terminated:
            return acc


if __name__ == "__main__":
    from aocd.models import Puzzle

    puzzle = Puzzle(2020, 8)
    program = clean_input(puzzle.input_data)

    puzzle.answer_a = part1(program)
    puzzle.answer_b = part2(program)
