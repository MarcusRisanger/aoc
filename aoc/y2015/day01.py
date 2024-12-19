def part1(inp: str) -> int:
    return inp.count("(") - inp.count(")")


def part2(inp: str) -> int:  # type: ignore[return]
    for i in range(len(inp)):
        if part1(inp[:i]) == -1:
            return i


if __name__ == "__main__":
    from aocd.models import Puzzle

    # Get puzzle details and set up input
    puzzle = Puzzle(year=2015, day=1)

    # Submit answers
    puzzle.answer_a = str(part1(puzzle.input_data))
    puzzle.answer_b = str(part2(puzzle.input_data))
