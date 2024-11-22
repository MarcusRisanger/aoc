from collections.abc import Sequence


def clean_input(inp: str) -> tuple[int, ...]:
    return tuple(map(int, inp.split(",")))


def recite(seed: Sequence[int], n: int) -> str:
    spoken, last = {s: i for i, s in enumerate(seed[:-1])}, seed[-1]
    for i in range(len(seed), n):
        if last not in spoken:
            new = 0
        else:
            new = i - 1 - spoken[last]
        spoken[last] = i - 1
        last = new
    return str(last)


if __name__ == "__main__":
    from aocd.models import Puzzle

    puzzle = Puzzle(2020, 15)

    seed = clean_input(puzzle.input_data)

    puzzle.answer_a = recite(seed, 2020)
    puzzle.answer_b = recite(seed, 30_000_000)
