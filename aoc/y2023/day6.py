from math import prod


def clean_input(input: str) -> tuple[list[int], list[int]]:
    inp = input.split("\n")
    return [line.split()[1:] for line in inp]


def race(time, record) -> int:
    return sum(1 if t0 * (time - t0) > record else 0 for t0 in range(time))


def part1(times: list[int], records: list[int]) -> int:
    return prod(race(t, r) for t, r in zip(map(int, times), map(int, records)))


def part2(times: list[int], records: list[int]) -> int:
    return race(int("".join(times)), int("".join(records)))


if __name__ == "__main__":
    from aocd.models import Puzzle

    # Get puzzle details and set up input
    puzzle = Puzzle(year=2023, day=6)

    times, records = clean_input(puzzle.input_data)

    # Submitting answers
    puzzle.answer_a = part1(times, records)
    puzzle.answer_b = part2(times, records)
