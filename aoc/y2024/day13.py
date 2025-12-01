import re

A = int
B = int
Claw = tuple[int, ...]


def clean_input(inp: str) -> list[Claw]:
    return [[*map(int, re.findall(r"(\d+)", claw))] for claw in inp.split("\n\n")]


def cost(claw: Claw, p2: bool = False) -> int:
    ax, ay, bx, by, tx, ty = claw

    tx = tx + 10000000000000 if p2 else tx
    ty = ty + 10000000000000 if p2 else ty

    b = (ty * ax - tx * ay) / (by * ax - bx * ay)
    a = (tx - b * bx) / ax

    if all(x.is_integer() for x in (a, b)):
        return 3 * int(a) + int(b)  # Let's assume the cheapest way is... the only way

    return 0  # Unsolvable


def part1(claws: list[Claw]) -> int:
    return sum(map(cost, claws))


def part2(claws: list[Claw]) -> int:
    return sum(map(cost, claws, [True] * len(claws)))


if __name__ == "__main__":
    from aocd.models import Puzzle

    # Get puzzle details and set up input
    puzzle = Puzzle(year=2024, day=13)

    input_data = clean_input(puzzle.input_data)

    # Submit answers
    puzzle.answer_a = str(part1(input_data))
    puzzle.answer_b = str(part2(input_data))
