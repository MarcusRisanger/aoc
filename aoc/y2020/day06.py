

def clean_input(inp: str) -> list[list[str]]:
    return [line.splitlines() for line in inp.split("\n\n")]


def part1(groups: list[list[str]]) -> str:
    """
    For each group of answers, checks if each distinct answer exists.
    Create a set of the letters found within a group, sum length of sets.
    """
    return str(sum(len(set("".join(group))) for group in groups))


def part2(groups: list[list[str]]) -> str:
    """
    Count only answers that exist for all members in group.
    Find the intersection of all the subsets of the group, sum lengths of intersections.
    """
    return str(sum(len(set.intersection(*map(set, group))) for group in groups))


if __name__ == "__main__":
    from aocd.models import Puzzle

    # Get puzzle details and set up input
    puzzle = Puzzle(year=2020, day=6)

    input_data = clean_input(puzzle.input_data)

    # Submit answers
    puzzle.answer_a = part1(input_data)
    puzzle.answer_b = part2(input_data)
