from functools import cache

Coord = complex


def clean_input(inp: str) -> tuple[Coord, tuple[Coord, ...], int]:
    lines = inp.splitlines()
    s = complex(lines[0].find("S"))
    splitters = tuple([complex(x, y) for y, row in enumerate(lines[1:], 1) for x, val in enumerate(row) if val == "^"])

    return s, splitters, len(lines)


def part1(s, splitters, num_lines) -> int:
    beams = {s}
    splitters_hit = 0
    for i in range(1, num_lines):
        beams = {b + 1j for b in beams}  # Move all beams down
        sp = {s for s in splitters if s in beams}  # Find splitter @ beams

        new_beams = {s + i for s in sp for i in {1, -1}}  # Split beams
        beams.update(new_beams)
        beams -= sp  # Remove splitters from beams

        splitters_hit += len(sp)
    return splitters_hit


@cache
def get_max(splitters: tuple[Coord]) -> int:
    return max(int(s.imag) for s in splitters)


@cache
def count_possibilities(b: Coord, splitters: tuple[Coord, ...]) -> int:
    if b.imag == max(s.imag for s in splitters):
        return 1
    elif b + 1j in splitters:
        return sum(count_possibilities(b + i, splitters) for i in (1, -1))
    else:
        return count_possibilities(b + 1j, splitters)


def part2(s: Coord, splitters: tuple[Coord, ...]) -> int:
    return count_possibilities(s, splitters)


if __name__ == "__main__":
    from aocd.models import Puzzle

    # Get puzzle details and set up input
    puzzle = Puzzle(year=2025, day=7)
    input_data = puzzle.input_data

    s, splitters, num_lines = clean_input(input_data)

    # Submit answers
    puzzle.answer_a = str(part1(s, splitters, num_lines))
    puzzle.answer_b = str(part2(s, splitters))
