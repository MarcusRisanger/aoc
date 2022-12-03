from string import ascii_letters


def clean_input(input_data: str) -> list[tuple[str, str]]:
    return [(r[: len(r) // 2], r[len(r) // 2 :]) for r in input_data.splitlines()]


def part1(data: list[tuple[str, str]]) -> int:
    """Returns sum of priorities of misplaced items in rucksacks."""
    return sum([ascii_letters.index(next(iter(set(a) & set(b)))) + 1 for a, b in data])


def part1_verbose(data: list[tuple[str, str]]) -> int:
    """Returns sum of priorities of misplaced items in rucksacks.
    Verbose solution to make steps clearer."""
    all_letters = ascii_letters
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
    """Returns sum of priorities of shared items across groups of three
    contiguous rucksacks."""
    groups = [data[i : i + 3] for i in range(0, len(data), 3)]
    out = 0
    for group in groups:
        # Taking advantage of unpacking the list containing the sets of stuff
        sets = set.intersection(*[set("".join(g)) for g in group])
        out += ascii_letters.index(next(iter(sets))) + 1
    return out


if __name__ == "__main__":
    from aocd.models import Puzzle

    # Get puzzle details and set up input
    puzzle = Puzzle(year=2022, day=3)
    input_data = clean_input(puzzle.input_data)

    # Submit answers
    puzzle.answer_a = part1(input_data)
    puzzle.answer_b = part2(input_data)
