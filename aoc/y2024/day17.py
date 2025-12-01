import re


def clean_input(inp: str) -> tuple[list[int], int, int, int]:
    a, b, c, *inst = [*map(int, re.findall(r"(\d+)", inp))]
    return inst, a, b, c


def run(instructions: list[int], A: int, B: int, C: int) -> list[int]:
    pointer = 0
    out: list[int] = []
    while pointer < len(instructions):
        reg = {0: 0, 1: 1, 2: 2, 3: 3, 4: A, 5: B, 6: C}
        opcode, operand = instructions[pointer : pointer + 2]
        match opcode:
            case 0:
                # Same as A // 2 ** reg[operand]
                A = A >> reg[operand]
            case 1:
                B = B ^ operand
            case 2:
                B = reg[operand] % 8
            case 3:
                pointer = operand - 2 if A else pointer
            case 4:
                B = B ^ C
            case 5:
                out.append(reg[operand] % 8)
            case 6:
                B = A >> reg[operand]
            case 7:
                C = A >> reg[operand]
        pointer += 2

    return out


def part1(instructions: list[int], A: int, B: int, C: int) -> str:
    return ",".join([*map(str, run(instructions, A, B, C))])


def part2(instructions) -> int:
    """
    Works backward to check for A that satisfies outputs.

    For instance: Let's say the program ends with [...,5,3,0].

    First it will find which value 0-7 that will output [0],
    which is A = 5. This value is multiplied by 8 and stored in the queue
    along with the required next sublength (2) to check against program output.

    For the next index, we find which value 0-7 to add to (5*8) that gives
    output [3,0] - this includes A=42 and A=47. Both of these are added to the
    queue after multiplying by 8. We now have two "seeds" to track backward from.

    We check A=42..49 and A=47..54 for program outputs of [5,3,0] .. etc.

    When we are at the last index, we will have several values for A that satisfy
    the requirement, so we put all A's into a list and return the smallest value.
    """

    search: list[tuple[int, int]] = [(1, 0)]
    possible: list[int] = list()
    while search:
        i, a = search.pop()
        for a in range(a, a + 8):
            out = run(instructions, a, 0, 0)
            if out == instructions:
                possible.append(a)
            elif out == instructions[-i:]:
                search.append((i + 1, a * 8))
    return min(possible)


if __name__ == "__main__":
    from aocd.models import Puzzle

    # Get puzzle details and set up input
    puzzle = Puzzle(year=2024, day=17)
    data = clean_input(puzzle.input_data)

    # Submit answers
    puzzle.answer_a = part1(*data)
    puzzle.answer_b = str(part2(data[0]))
