def clean_input(inp: str) -> list[int]:
    """Splits input into the two `Location` lists."""
    return [*map(int, inp.translate(str.maketrans("RL", "+-")).splitlines())]


def part1(inp: str) -> int:
    """Times the pointer stops at position 0"""
    tot = 0
    for row in inp.split(","):
        a, b = map(int, row.split("-"))
        for i in range(a, b + 1):
            id = str(i)
            if id[: len(id) // 2] == id[len(id) // 2 :]:
                tot += i

    return tot


def check_id(id: str):
    return any(id.count(id[:i]) == len(id) / len(id[:i]) for i in range(1, 1 + len(id) // 2))


def part2(inp: str) -> int:
    tot = 0
    for row in inp.split(","):
        a, b = map(int, row.split("-"))
        for i in range(a, b + 1):
            if check_id(str(i)):
                tot += i
    return tot


if __name__ == "__main__":
    from aocd.models import Puzzle

    # Get puzzle details and set up input
    puzzle = Puzzle(year=2025, day=2)
    input_data = puzzle.input_data

    # Submit answers
    puzzle.answer_a = str(part1(input_data))
    puzzle.answer_b = str(part2(input_data))
