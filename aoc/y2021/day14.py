from collections import defaultdict


def polymer(input_data: str):

    template, rules = input_data.split("\n\n")
    rules = dict(i.split(" -> ") for i in rules.splitlines())

    pairs = defaultdict(int)
    for i, j in zip(template, template[1:]):
        pairs[i + j] += 1

    chars = defaultdict(int)
    for i in template:
        chars[i] += 1

    for i in range(40):
        for (a, b), c in pairs.copy().items():
            x = rules[a + b]
            pairs[a + b] -= c
            pairs[a + x] += c
            pairs[x + b] += c
            chars[x] += c

        if i == 9:
            part1 = max(chars.values()) - min(chars.values())
    part2 = max(chars.values()) - min(chars.values())

    return part1, part2


if __name__ == "__main__":
    from aocd.models import Puzzle

    puzzle = Puzzle(2021, 14)
    input_data = puzzle.input_data

    puzzle.answer_a, puzzle.answer_b = polymer(input_data)
