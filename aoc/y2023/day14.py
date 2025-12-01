from collections.abc import Sequence
from functools import cache
import re
from typing import Iterable, Literal


def transform_data(inp: str) -> tuple[str, ...]:
    return tuple(inp.splitlines())


def transpose(dish: Sequence[str]) -> tuple[str, ...]:
    """Transposes array."""
    return tuple(
        "".join(dish[r][c] for r in range(len(dish))) for c in range(len(dish[0]))
    )


def split_line(line: str) -> list[tuple[str, ...]]:
    """
    Splits a line into contiguous parts of:
      - Cube-shaped rocks (#)
      - Rounded rocks (O) and empty spaces (.)
    """
    return re.findall(r"(?:\#+|[O\.]+)", line)


@cache
def sort_rocks(element: str, reverse: bool) -> str:
    """For a given element, sort to order."""
    if "#" in element:
        return element
    return "".join(sorted(element, reverse=reverse))


def process_line(arg: str, reverse: bool) -> str:
    return "".join([sort_rocks(a, reverse) for a in split_line(arg)])


def tilt_ns(dish: Sequence[str], dir: Literal["n", "s"] = "n") -> tuple[str, ...]:
    """
    For tilting north/south we transpose the dish before and after processing lines.
    """
    if dir == "n":
        reverse = True
    else:
        reverse = False
    dish_t = transpose(dish)
    tilted = [process_line(line, reverse=reverse) for line in dish_t]
    return transpose(tilted)


def tilt_ew(dish: Sequence[str], dir: Literal["e", "w"]) -> tuple[str, ...]:
    """
    For tilting east/west we don't have to transpose the dish argument.
    """
    if dir == "w":
        reverse = True
    else:
        reverse = False
    return tuple(process_line(line, reverse) for line in dish)


@cache
def cycle(dish: Sequence[str]) -> tuple[str, ...]:
    """
    Cycles the dish N, W, S, E, according to specifications.
    """
    dish = tilt_ns(dish, dir="n")
    dish = tilt_ew(dish, dir="w")
    dish = tilt_ns(dish, dir="s")
    return tilt_ew(dish, dir="e")


def total_load(dish: Iterable[str]):
    """
    The total load is calculated as the count of `O` per row, multiplied by a factor
    that equals the total row count minus the current row index.
    """
    return sum(line.count("O") * (len(dish) - i) for i, line in enumerate(dish))  # type: ignore


def cycle_dish(dish: tuple[str, ...], num_loops: int) -> str:
    """
    We assume that there is looping here, since the number of cycles is so high (1 billion).

    We store each dish configuration in a dictionary as a key (big key!) along with the value
    of the cycle number. If we arrive at a rock distribution that we have seen before, we
    can "skip" a lot of cycles depending on three factors:

    - The total number of cycles
    - The cycle number when the config was first seen
    - The current cycle number

    First we establish the `loop_size`, which is the current cycle minus the cycle number
    when this rock configuration was first seen. Using the current cycle and the number of loops,
    we can find how many cycles are remaining. We use the loop size as modulus on this remainder
    to see how many cycles we have left outstanding to arrive at max cycles.

    We cycle for the remainder and calculate the load on the resulting dish configuration.
    """

    seen_cycle = dict()
    current_cycle = 0

    while True:
        seen_cycle[dish] = current_cycle
        dish = cycle(dish)
        current_cycle += 1

        if dish in seen_cycle:
            loop_size = (
                current_cycle - seen_cycle[dish]
            )  # Current cycle minus cycle where dish was seen first
            cycles_left = (num_loops - current_cycle) % loop_size
            break

    for _ in range(cycles_left):
        dish = cycle(dish)

    return str(total_load(dish))


def part1(inp: str) -> str:
    dish = transform_data(inp)
    return str(total_load(tilt_ns(dish)))


def part2(inp: str, cycles: int) -> str:
    dish = transform_data(inp)
    return cycle_dish(dish, cycles)


if __name__ == "__main__":
    from aocd.models import Puzzle

    puzzle = Puzzle(2023, 14)

    puzzle.answer_a = part1(puzzle.input_data)
    puzzle.answer_b = part2(puzzle.input_data, 1_000_000_000)
