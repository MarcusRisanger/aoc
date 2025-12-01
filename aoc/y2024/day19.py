from functools import cache, partial

Recipe = str
Towel = str


def clean_input(inp: str) -> tuple[list[Recipe], tuple[Towel, ...]]:
    t, r = inp.split("\n\n")
    return r.splitlines(), tuple(t.split(", "))


@cache
def possible(recipe: str, towels: tuple[str, ...]):
    if not recipe:
        return True
    return sum(possible(recipe.removeprefix(t), towels) for t in towels if recipe.startswith(t))


def part1(recipes: list[Recipe], towels: tuple[Towel, ...]) -> int:
    func = partial(possible, towels=towels)
    return sum(1 for r in map(func, recipes) if r)


def part2(recipes: list[Recipe], towels: tuple[Towel, ...]) -> int:
    func = partial(possible, towels=towels)
    return sum(map(func, recipes))


if __name__ == "__main__":
    from aocd.models import Puzzle

    # Get puzzle details and set up input
    puzzle = Puzzle(year=2024, day=19)
    data = clean_input(puzzle.input_data)

    # Submit answers
    puzzle.answer_a = str(part1(*data))
    puzzle.answer_b = str(part2(*data))
