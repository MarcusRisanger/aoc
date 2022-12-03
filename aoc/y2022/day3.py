from string import ascii_lowercase as lower, ascii_uppercase as upper


def clean_input(input_data: str) -> list[tuple[str, str]]:
    return [(r[: len(r) // 2], r[len(r) // 2 :]) for r in input_data.splitlines()]


def part1(data: list[tuple[str, str]]) -> int:
    """Returns sum of priorities of misplaced items in rucksacks."""
    prios = {k: v + 1 for v, k in enumerate(lower + upper)}
    return sum([prios[next(iter(set(a) & set(b)))] for a, b in data])


def part1_verbose(data: list[tuple[str, str]]) -> int:
    all_letters = lower + upper
    priorities = dict()
    for i, letter in enumerate(all_letters):
        priorities[letter] = i + 1

    prio_sum = 0
    for rucksack_contents in data:
        comp1, comp2 = set(rucksack_contents[0]), set(rucksack_contents[1])
        in_both = comp1.intersection(comp2)
        item = list(in_both)[0]
        item_value = priorities[item]
        prio_sum += item_value

    return prio_sum


def part2(data: list[str]):
    prios = {k: v + 1 for v, k in enumerate(lower + upper)}
    pass


if __name__ == "__main__":
    from aocd.models import Puzzle

    # Get puzzle details and set up input
    puzzle = Puzzle(year=2022, day=3)
    input_data = clean_input(puzzle.input_data)

    # Submit answers
    puzzle.answer_a = part1(input_data)
    # puzzle.answer_b = part2(input_data)
