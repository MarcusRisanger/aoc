from re import findall

Location = int


def clean_input(inp: str) -> tuple[list[Location], list[Location]]:
    """Splits input into the two `Location` lists."""
    ns = [*map(int, findall(r"\d+", inp))]
    return ns[::2], ns[1::2]


def part1(l1: list[Location], l2: list[Location]) -> int:
    """Finds the total difference between sorted lists."""
    return sum(abs(a - b) for a, b in zip(sorted(l1), sorted(l2)))


def part2(l1: list[Location], l2: list[Location]) -> int:
    """Finds the similarity score between lists."""
    return sum(a * l2.count(a) for a in l1)


if __name__ == "__main__":
    from aocd.models import Puzzle

    # Get puzzle details and set up input
    puzzle = Puzzle(year=2024, day=1)
    input_data = clean_input(puzzle.input_data)

    # Submit answers
    puzzle.answer_a = str(part1(*input_data))
    puzzle.answer_b = str(part2(*input_data))
