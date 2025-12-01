def clean_input(inp: str) -> list[int]:
    """Splits input into the two `Location` lists."""
    return [*map(int, inp.translate(str.maketrans("RL", "+-")).splitlines())]


def part1(inp: list[int]) -> int:
    """Times the pointer stops at position 0"""
    return sum(1 for p in [50 + sum(inp[:i]) for i in range(len(inp) + 1)] if p % 100 == 0)


def get_spins(start, end) -> int:
    if start < end:  # cw
        spins = (end // 100) - (start // 100)
    if start > end:  # ccw
        spins = (start // 100) - (end // 100)
        spins -= 1 if start % 100 == 0 else 0
        spins += 1 if end % 100 == 0 else 0
    return spins


def part2(inp: list[int]) -> int:
    positions = [50 + sum(inp[:i]) for i in range(len(inp) + 1)]
    return sum(get_spins(x, y) for x, y in zip(positions, positions[1:]))


if __name__ == "__main__":
    from aocd.models import Puzzle

    # Get puzzle details and set up input
    puzzle = Puzzle(year=2025, day=1)
    input_data = clean_input(puzzle.input_data)

    # Submit answers
    puzzle.answer_a = str(part1(input_data))
    puzzle.answer_b = str(part2(input_data))
