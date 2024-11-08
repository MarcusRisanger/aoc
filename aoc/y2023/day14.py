from functools import cache
import re


def transform_data(inp: str) -> list[str]:
    return inp.splitlines()


def transpose(dish: list[str]) -> list[str]:
    """Transposes array."""
    return [
        "".join([dish[r][c] for r in range(len(dish))]) for c in range(len(dish[0]))
    ]


def split_line(line: str) -> tuple[str, ...]:
    """
    Splits a line into contiguous parts of:
      - Cube-shaped rocks (#)
      - Rounded rocks (O) and empty spaces (.)
    """
    return re.findall(r"(?:\#+|[O\.]+)", line)


@cache
def sort_rocks(element: str) -> str:
    """For a given element, sort"""
    if "#" in element:
        return element
    return "".join(sorted(element)[::-1])


def process_line(arg: str) -> str:
    return "".join(list(map(sort_rocks, split_line(arg))))


def tilt_north(dish: list[str]) -> list[str]:
    dish_t = transpose(dish)
    tilted = [process_line(line) for line in dish_t]
    return transpose(tilted)


def score_rocks(dish: list[str]):
    return sum(line.count("O") * (len(dish) - i) for i, line in enumerate(dish))


def part1(inp: str) -> str:
    dish = transform_data(inp)
    return str(score_rocks(tilt_north(dish)))


if __name__ == "__main__":
    from aocd.models import Puzzle

    puzzle = Puzzle(2023, 14)

    puzzle.answer_a = part1(puzzle.input_data)
