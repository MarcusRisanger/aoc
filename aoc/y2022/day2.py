def clean_input(data: str) -> list[tuple[str, str]]:
    """Cleans input data into pairs of instructions."""
    return [tuple(i.split()) for i in data.splitlines()]


def points(
    opponent: str,
    player: str,
) -> int:
    """
    Simple function to output player score based on choice, outcome.

    A / X = Opponent / Player throws rock
    B / Y = Opponent / Player throws paper
    C / Z = Opponent / Player throws scissors
    """
    # Scores for outcomes, choices
    outcomes = {"w": 6, "d": 3, "l": 0}
    choices = {"r": 1, "p": 2, "s": 3}
    o, c = outcomes, choices

    # Let's do it simple..
    score = {
        "A": {"X": c["r"] + o["d"], "Y": c["p"] + o["w"], "Z": c["s"] + o["l"]},
        "B": {"X": c["r"] + o["l"], "Y": c["p"] + o["d"], "Z": c["s"] + o["w"]},
        "C": {"X": c["r"] + o["w"], "Y": c["p"] + o["l"], "Z": c["s"] + o["d"]},
    }
    return score[opponent][player]


def part1(data: list[tuple[str, str]]) -> int:
    """What will be the player score if you follow the instructions?"""
    return sum([points(*throws) for throws in data])


def part2(data: list[list[int]]) -> int:
    """What will be the player score if you shape throw according to instructions?"""

    def answer(opponent, outcome):
        """
        Translating outcome to player throw - bit messy since there are a lot
        of Xs and Ys and Zs.

        A / X = Opponent / Player must lose
        B / Y = Opponent / Player must draw
        C / Z = Opponent / Player must win
        """
        throw = {
            "A": {"X": "Z", "Y": "X", "Z": "Y"},
            "B": {"X": "X", "Y": "Y", "Z": "Z"},
            "C": {"X": "Y", "Y": "Z", "Z": "X"},
        }
        return throw[opponent][outcome]

    return sum(
        [points(opponent, answer(opponent, outcome)) for opponent, outcome in data]
    )


if __name__ == "__main__":
    from aocd.models import Puzzle

    # Get puzzle details and set up input
    puzzle = Puzzle(year=2022, day=2)
    input_data = clean_input(puzzle.input_data)

    # Submit answers
    puzzle.answer_a = part1(input_data)
    puzzle.answer_b = part2(input_data)
