def get_id(seat: str) -> int:
    """Translate boarding pass to seat ID."""
    table = str.maketrans("FLBR", "0011")  # Translate to binary number
    return int(seat.translate(table), base=2)


def part1(inp: str) -> str:
    """Get the max seat ID."""
    return str(max(map(get_id, (seat for seat in inp.splitlines()))))


def part2(inp: str) -> str:
    # Calculate all IDs
    ids: set[int] = set(map(get_id, (seat for seat in inp.splitlines())))

    # Identify the one missing value within set
    [missing] = set(range(min(ids), max(ids))) - ids
    return str(missing)


if __name__ == "__main__":
    from aocd.models import Puzzle

    # Get puzzle details and set up input
    puzzle = Puzzle(year=2020, day=5)

    # Submit answers
    puzzle.answer_a = part1(puzzle.input_data)
    puzzle.answer_b = part2(puzzle.input_data)
