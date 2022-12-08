def clean_input(input_data: str) -> dict[tuple[int, int], int]:
    return {
        (x, y): val
        for x, line in enumerate(input_data.splitlines())
        for y, val in enumerate(line)
    }


def is_visible(grid: dict[tuple[int, int], int], r: int, c: int):
    x_max, y_max = max(grid)
    return any(
        [
            all((grid[n] < grid[r, c]) for n in [(x + 1, c) for x in range(r, x_max)]),
            all((grid[n] < grid[r, c]) for n in [(x, c) for x in range(0, r)]),
            all((grid[n] < grid[r, c]) for n in [(r, y + 1) for y in range(c, y_max)]),
            all((grid[n] < grid[r, c]) for n in [(r, y) for y in range(0, c)]),
        ]
    )


def part1(input_data: dict[tuple[int, int], int]) -> int:
    return sum(is_visible(input_data, *n) for n in input_data)


def scenic_score(grid: dict[tuple[int, int], int], r: int, c: int) -> int:
    value = grid[(r, c)]
    score = 1
    for x, y in ((-1, 0), (1, 0), (0, -1), (0, 1)):
        step = 1
        while True:
            try:
                if value <= grid[r + (x * step), c + (y * step)]:
                    break
            except:
                step -= 1
                break
            step += 1
        score *= step
    return score


def part2(input_data: dict[tuple[int, int], int]) -> int:
    return max(scenic_score(input_data, *n) for n in input_data)


if __name__ == "__main__":
    from aocd.models import Puzzle
    from time import time

    # Get puzzle details and set up input
    puzzle = Puzzle(year=2022, day=8)
    input_data = clean_input(puzzle.input_data)

    # Submit answers
    puzzle.answer_a = part1(input_data)
    puzzle.answer_b = part2(input_data)
