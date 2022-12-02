def clean_input(data: str) -> list[str]:
    """Cleans input data into pairs of instructions."""
    return [i.replace(" ", "") for i in data.splitlines()]


def part1(data: list[str]) -> int:
    """What will be the player score if you follow the instructions?"""
    # Set up result combinations ordered by increasing score
    # Find score by integer division of game index in string
    scores = "  BXCYAZAXBYCZCXAYBZ"
    return sum([scores.index(game) // 2 for game in data])


def part2(data: list[str]) -> int:
    """What will be the player score if you shape throw according to instructions?"""
    scores = "  BXCXAXAYBYCYCZAZBZ"
    return sum([scores.index(game) // 2 for game in data])


if __name__ == "__main__":
    from aocd.models import Puzzle

    # Get puzzle details and set up input
    puzzle = Puzzle(year=2022, day=2)
    input_data = clean_input(puzzle.input_data)

    # Submit answers
    puzzle.answer_a = part1(input_data)
    puzzle.answer_b = part2(input_data)
