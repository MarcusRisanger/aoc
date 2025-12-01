def clean_input(data: str) -> list[int]:
    """Cleans input data using simple splits.
    Splits string into blocks on double line break.
    Sums the integers of each block, output contains
    one list element per elf."""
    return [sum(map(int, b.split("\n"))) for b in data.split("\n\n")]


def part1(data: list[int]) -> int:
    """How many calories are carried by the
    elf that carries the most calories?"""
    return max(data)


def part2(data: list[list[int]]) -> int:
    """How many calories are carried in total by
    the three elves carrying the most calories?"""
    return sum(sorted(data, reverse=True)[:3])


if __name__ == "__main__":
    from aocd.models import Puzzle

    # Get puzzle details and set up input
    puzzle = Puzzle(year=2022, day=1)
    input_data = clean_input(puzzle.input_data)

    # Submit answers
    puzzle.answer_a = part1(input_data)
    puzzle.answer_b = part2(input_data)
