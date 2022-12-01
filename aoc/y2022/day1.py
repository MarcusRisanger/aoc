def clean_input(data: str) -> list[list[int]]:
    out = [[]]
    for row in data.splitlines():
        if row == "":
            out.append([])
        else:
            out[-1].append(int(row))
    return out


def part1(data: list[list[int]]) -> int:
    """How many calories are carried by the
    elf that carries the most calories?"""
    return max(sum(i) for i in data)


def part2(data: list[list[int]]) -> int:
    """How many calories are carried in total by
    the three elves carrying the most calories?"""
    return sum(sorted([sum(i) for i in data], reverse=True)[:3])


if __name__ == "__main__":
    from aocd.models import Puzzle

    # Get puzzle details and set up input
    puzzle = Puzzle(year=2022, day=1)
    input_data = clean_input(puzzle.input_data)

    # Submit answers
    puzzle.answer_a = part1(input_data)
    puzzle.answer_b = part2(input_data)
