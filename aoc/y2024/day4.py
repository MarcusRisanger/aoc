def part1(inp: str) -> int:
    """Count occurrences of "XMAS" where all directions are valid."""
    row = inp.index("\n")  # Row width for slicing
    return sum(
        w in ("XMAS", "SAMX")
        for i in range(len(inp))
        for w in (
            inp[i : i + 4],  # Straight (—)
            inp[i::row][:4],  # Diagonal (/)
            inp[i :: row + 1][:4],  # Down (|)
            inp[i :: row + 2][:4],  # Diagonal (\)
        )
    )


def part2(inp: str) -> int:
    """Count occurrences where both diagonals across A make "MAS" or "SAM"."""
    row = inp.index("\n")
    return sum(
        all(
            w in ("MAS", "SAM")
            for w in (
                inp[i - row : i + row + 1 : row],  # Diagonal (/)
                inp[i - (row + 2) : i + (row + 2) + 1 : row + 2],  # Diagonal (\)
            )
        )
        for i in range(len(inp))
    )


if __name__ == "__main__":
    from aocd.models import Puzzle

    # Get puzzle details and set up input
    puzzle = Puzzle(year=2024, day=4)

    # Submit answers
    puzzle.answer_a = str(part1(puzzle.input_data))
    puzzle.answer_b = str(part2(puzzle.input_data))
