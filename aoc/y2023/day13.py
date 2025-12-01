from collections.abc import Sequence, Generator, Iterable
from functools import partial
from typing import Literal


def get_slices(
    pattern: Sequence[str], dir: Literal["row", "col"]
) -> Generator[tuple[int, list[int], list[int]], None, None]:
    """
    Get slices for evaluating input from pattern between rows 0 and 1 and onwards.

    For evaluating row zero, the script must compare row 0 with row 1 for equality.
    For evaluating row one, the script must compare rows 0,1 with rows 3,2 for equality.
    """
    if dir == "row":
        length = len(pattern)
    else:
        length = len(pattern[0])
    for i in range(1, length):
        right = [i for i in range(i, length)][:i][::-1]
        left = [i for i in range(0, i)][-len(right) :]
        yield i, right, left


def count_diffs(list1: Iterable[str], list2: Iterable[str]) -> int:
    """Counts all occurrences where the same index of both lists have differing symbols."""
    total = 0
    for a, b in zip(list1, list2):
        if a != b:
            total += 1
    return total


def pattern_horizontal_score(pattern: Sequence[str], target: int = 0) -> int:
    """Returns the horizontal score for the pattern."""
    for i, right, left in get_slices(pattern, "row"):
        if (
            sum(count_diffs(pattern[a], pattern[b]) for a, b in zip(right, left))
            == target
        ):
            return i * 100
    return 0


def pattern_vertical_score(pattern: Sequence[str], target: int = 0) -> int:
    """Returns the vertical score for the pattern."""
    for i, top, bottom in get_slices(pattern, "col"):
        if (
            sum(
                count_diffs(get_col(pattern, a), get_col(pattern, b))
                for a, b in zip(top, bottom)
            )
            == target
        ):
            return i
    return 0


def get_col(pattern: Iterable[str], col: int):
    """Shorthand to extract a full column from a tile."""
    return [row[col] for row in pattern]


def parse_pattern(pattern: str, target) -> int:
    """Parses a pattern into rows of strings, then returns the pattern score."""
    pat = [c for c in pattern.splitlines()]
    return pattern_vertical_score(pat, target) + pattern_horizontal_score(pat, target)


def parse_input(arg: str) -> list[str]:
    """
    Split the input on double newline symbols.
    Each element in the returned list represents a pattern.
    """
    return arg.split("\n\n")


def part1(arg: str) -> str:
    """Get score of patterns, expecting zero flaws."""
    func = partial(parse_pattern, target=0)
    return str(sum(map(func, parse_input(arg))))


def part2(arg: str) -> str:
    """Get score of patterns, expecting one flaw per pattern."""
    func = partial(parse_pattern, target=1)
    return str(sum(map(func, parse_input(arg))))


if __name__ == "__main__":
    from aocd.models import Puzzle

    puzzle = Puzzle(2023, 13)
    puzzle.answer_a = part1(puzzle.input_data)
    puzzle.answer_b = part2(puzzle.input_data)
