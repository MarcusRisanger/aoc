def transform_input(inp: str) -> list[str]:
    return inp.splitlines()


def expand_galaxy_rows(inp: list[str]) -> list[int]:
    out = []
    for i, row in enumerate(inp):
        if all(v == "." for v in row):
            out.append(i)
    return out


def expand_galaxy_cols(inp: list[str]) -> list[int]:
    out = []
    for c in range(len(inp[0])):
        if all(inp[r][c] == "." for r in range(len(inp))):
            out.append(c)
    return out


def get_galaxies(inp: list[str]) -> set[tuple[int, int]]:
    galaxies = set()
    for r, row in enumerate(inp):
        for c, val in enumerate(row):
            if val == "#":
                galaxies.add((r, c))
    return galaxies


def get_path_length(
    current: tuple,
    other: tuple,
    row_expando: list[int],
    col_expando: list[int],
    spacing: int,
):
    row_ranges = sum(
        spacing if i in row_expando else 1
        for i in range(current[0], other[0], 1 if current[0] < other[0] else -1)
    )
    col_ranges = sum(
        spacing if i in col_expando else 1
        for i in range(current[1], other[1], 1 if current[1] < other[1] else -1)
    )
    return row_ranges + col_ranges


def sum_shortest_paths(galaxies: set[tuple[int, int]], row_exp, col_exp, factor) -> int:
    galaxy_copy = galaxies.copy()
    total = 0
    while galaxy_copy:
        current = galaxy_copy.pop()
        total += sum(
            get_path_length(current, other, row_exp, col_exp, factor)
            for other in galaxy_copy
        )
    return total


def shortest_paths(inp: str, factor: int = 2) -> int:
    space = transform_input(inp)
    row_exp = expand_galaxy_rows(space)
    col_exp = expand_galaxy_cols(space)
    galaxies = get_galaxies(space)
    return sum_shortest_paths(galaxies, row_exp, col_exp, factor)


def part1(inp: str) -> int:
    return shortest_paths(inp)


def part2(inp: str) -> int:
    return shortest_paths(inp, 1_000_000)


if __name__ == "__main__":
    from aocd.models import Puzzle

    # Get puzzle details and set up input
    puzzle = Puzzle(year=2023, day=11)

    # Submitting answers
    puzzle.answer_a = part1(puzzle.input_data)
    puzzle.answer_b = part2(puzzle.input_data)
