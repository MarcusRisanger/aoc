from functools import cache

Joltage = int
Adapters = tuple[Joltage, ...]


def clean_input(inp: str) -> Adapters:
    """Parse adapter values and add outlet joltage (0) and device joltage (max+3) to sequence."""
    adapters = tuple(sorted(list(map(int, inp.split()))))
    return (0,) + adapters + (max(adapters) + 3,)


def part1(adapters: Adapters) -> str:
    """Finds joltage differences of sequential adapters."""
    diffs = [j - i for i, j in zip(adapters[:-1], adapters[1:])]
    return str(diffs.count(1) * diffs.count(3))


@cache
def number_of_paths_to_joltage(joltage: Joltage, adapters: Adapters):
    """Recursively find number of ways to reach given Joltage."""
    if joltage not in adapters:
        return 0  # Can't reach the current joltage
    if joltage == 0:
        return 1  # Pre-seeded one way to "reach" outlet
    return sum(
        number_of_paths_to_joltage(j, adapters) for j in range(joltage - 3, joltage)
    )


def part2(adapters: Adapters):
    """Number of ways to reach max Joltage."""
    return str(number_of_paths_to_joltage(max(adapters), adapters))


if __name__ == "__main__":
    from aocd.models import Puzzle

    puzzle = Puzzle(2020, 10)
    adapters = clean_input(puzzle.input_data)

    puzzle.answer_a = part1(adapters)
    puzzle.answer_b = part2(adapters)
