def clean_input(data: str) -> list[tuple[str, str]]:
    """Cleans input data using simple splits.
    Splits string into blocks on double line break.
    Sums the integers of each block, output contains
    one list element per elf."""
    return [tuple(i.split()) for i in data.splitlines()]


def scores(player: str, opponent: str):
    score = {
        "A": {"X": 1 + 3, "Y": 2 + 6, "Z": 3 + 0},
        "B": {"X": 1 + 0, "Y": 2 + 3, "Z": 3 + 6},
        "C": {"X": 1 + 6, "Y": 2 + 0, "Z": 3 + 3},
    }
    return score[opponent][player]


def part1(data: list[tuple[str, str]]) -> int:
    """How many calories are carried by the
    elf that carries the most calories?"""
    return sum([scores(player, opponent) for opponent, player in data])


def part2(data: list[list[int]]) -> int:
    """How many calories are carried in total by
    the three elves carrying the most calories?"""
    return sum(sorted(data, reverse=True)[:3])


if __name__ == "__main__":
    from aocd.models import Puzzle

    # Get puzzle details and set up input
    puzzle = Puzzle(year=2022, day=2)
    input_data = clean_input(puzzle.input_data)

    # Submit answers
    puzzle.answer_a = part1(input_data)
    # puzzle.answer_b = part2(input_data)
