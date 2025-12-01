Coord = tuple[int, int]
Heading = Coord
Move = str
dirs: dict[Move, Coord] = {"^": (0, -1), "<": (-1, 0), ">": (1, 0), "v": (0, 1)}


def move(inp: str) -> set[Coord]:
    current = (0, 0)
    seen: set[Coord] = {current}
    for move in inp:
        heading = dirs[move]
        current = current[0] + heading[0], current[1] + heading[1]
        seen.add(current)
    return seen


def part1(inp: str) -> int:
    return len(move(inp))


def part2(inp: str) -> int:
    return len(move(inp[::2]) | move(inp[1::2]))


if __name__ == "__main__":
    from aocd.models import Puzzle

    # Get puzzle details and set up input
    puzzle = Puzzle(year=2015, day=3)

    # Submit answers
    puzzle.answer_a = str(part1(puzzle.input_data))
    puzzle.answer_b = str(part2(puzzle.input_data))
