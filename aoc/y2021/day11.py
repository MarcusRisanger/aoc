"""
AOC 2021, Day 11:
  - Keeping track of neighbors and flashing
  - Parts 1 and 2 implements the same code with different exits
"""

from aoc.utils import neighbors as n, extract_neighbors

Octopus = tuple[int, int]
Level = int
Octopi = dict[Octopus, Level]


def clean_input(input_data: str) -> Octopi:
    """Prepares octopi grid using x, y coordinates and initial value."""
    return {
        (x, y): int(val)
        for x, line in enumerate(input_data.splitlines())
        for y, val in enumerate(line)
    }


def get_octopi(octo: Octopus, octopi: Octopi) -> list[Octopus]:
    """Returns the neighboring octopi (incl. diagonal)."""
    return extract_neighbors(octo, octopi, shape="box")


def octopi_flashes(octopi: Octopi) -> tuple[str, str]:  # type: ignore[return]
    flashes = 0
    for cycle in range(1, 1000):
        # Increment all octopi
        for i in octopi:
            octopi[i] += 1
        # Create set of flashing octopi
        flashing = {i for i in octopi if octopi[i] > 9}

        # Churning through all flashes
        while flashing:
            i = flashing.pop()
            octopi[i] = 0
            flashes += 1
            # Incrementing neighbors that are != 0
            for neighbor in get_octopi(i, octopi):
                octopi[neighbor] += 1
                # If neighbor is pushed to flash, add to set
                if octopi[neighbor] > 9:
                    flashing.add(neighbor)

        if cycle == 100:
            part1 = flashes
        if sum(octopi.values()) == 0:
            return str(part1), str(cycle)


if __name__ == "__main__":
    from aocd.models import Puzzle

    puzzle = Puzzle(2021, 11)
    input_data = clean_input(puzzle.input_data)

    puzzle.answer_a, puzzle.answer_b = octopi_flashes(input_data)
