import re
from functools import cache

Bag = str
BagRules = dict[Bag, dict[Bag, int]]


def parse_inner_bag(inner: str) -> tuple[Bag, int]:
    count, bag = inner.split(maxsplit=1)
    return bag, (0 if count == "no" else int(count))


def parse_rule(bag: str) -> tuple[Bag, dict[Bag, int]]:
    bag = re.sub(r" bags?|\.", "", bag)  # Cleans string from unwanted stuff
    outer, inner = bag.split(" contain ")
    return outer, dict(map(parse_inner_bag, inner.split(",")))


def clean_input(inp: str) -> BagRules:
    return dict(map(parse_rule, inp.splitlines()))


def part1(rules: BagRules) -> str:
    """Checks rules and counts all bags that can contain a shiny golden bag."""

    @cache
    def contains_bag(bag: Bag, target: Bag) -> bool:
        contents = rules.get(bag, dict())
        return target in contents or any(
            contains_bag(inner, target) for inner in contents
        )

    return str(sum(1 for bag in rules if contains_bag(bag, "shiny gold")))


def part2(rules: BagRules) -> str:
    """Checks rules and recursively sums all bags contained in a shiny golden bag."""

    @cache
    def bag_count(bag: Bag) -> int:
        return sum(n + n * bag_count(inner) for inner, n in rules[bag].items() if n > 0)

    return str(bag_count("shiny gold"))


if __name__ == "__main__":
    from aocd.models import Puzzle

    # Get puzzle details and set up input
    puzzle = Puzzle(year=2020, day=7)

    bag_rules = clean_input(puzzle.input_data)

    # Submit answers
    puzzle.answer_a = part1(bag_rules)
    puzzle.answer_b = part2(bag_rules)
