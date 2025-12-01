from collections.abc import Sequence
from itertools import combinations


def clean_input(inp: str) -> tuple[int, ...]:
    """Parses data into tuple of ints."""
    return tuple(map(int, inp.split()))


def next_number_valid(num: int, addends: Sequence[int]) -> bool:
    """Returns True if any pair in `addends` can be summed to `num`."""
    return any(num == n1 + n2 for n1, n2 in combinations(addends, 2))


def encryption_weakness(contiguous: Sequence[int]) -> str:
    """Definition of the encryption weakness for part 2."""
    return str(min(contiguous) + max(contiguous))


def part1(sequence: Sequence[int], preamble_length: int) -> str:  # type: ignore[return]
    for i in range(preamble_length, len(sequence)):
        current_number = sequence[i]
        addends = sequence[i - preamble_length : i]
        if not next_number_valid(current_number, addends):
            return str(sequence[i])


def part2(num: int, sequence: Sequence[int]):
    contiguous: list[int] = list()
    for i in range(len(sequence)):
        # Exit condition as defined in the task
        exit_condition = sum(contiguous) == num and len(contiguous) > 1
        if exit_condition:
            return encryption_weakness(contiguous)

        while sum(contiguous) + sequence[i] > num:
            # If we can't add next number to contiguous sequence without
            # going above the target value, we have to remove elements
            # from the beginning of the contiguous sequence
            contiguous.pop(0)

        contiguous.append(sequence[i])


if __name__ == "__main__":
    from aocd.models import Puzzle

    puzzle = Puzzle(2020, 9)
    sequence = clean_input(puzzle.input_data)

    puzzle.answer_a = part1(sequence, preamble_length=25)
    puzzle.answer_b = part2(int(puzzle.answer_a), sequence)
