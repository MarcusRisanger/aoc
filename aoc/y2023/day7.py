from collections import Counter


def hand(row: str, part=1) -> tuple[str, int]:
    hand, val = row.split()
    count = Counter(hand)
    if part == 2 and "J" in count.keys() and count.get("J") < 5:
        # Just shamelessly assuming it's fine to tack on the jokers to whatever
        # card nomination is the highest count outside of jokers...
        key = list(filter(lambda x: x[0] != "J", count.most_common()))[0][0]
        count[key] += count.pop("J")
    vals = sorted(count.values())
    match len(vals), max(vals):
        case 1, _:
            s = "A"  # 5 of a kind
        case 2, 4:
            s = "B"  # 4 of a kind
        case 2, 3:
            s = "C"  # Full house
        case 3, 3:
            s = "D"  # Three of a kind
        case 3, 2:
            s = "E"  # Two pairs
        case 4, 2:
            s = "F"  # One pair
        case 5, _:
            s = "G"  # High card
    return (s + hand), int(val)


def part1(input: str) -> int:
    tr = str.maketrans("AKQJT98765432", "ABCDEFGHIJKLM")
    ranks = sorted([hand(row) for row in input.splitlines()], key=lambda x: x[0].translate(tr))
    return sum(score[1] * (len(ranks) - i) for i, score in enumerate(ranks))


def part2(input: str) -> int:
    tr = str.maketrans("AKQT98765432J", "ABCDEFGHIJKLM")
    ranks = sorted([hand(row, 2) for row in input.splitlines()], key=lambda x: x[0].translate(tr))
    return sum(score[1] * (len(ranks) - i) for i, score in enumerate(ranks))


if __name__ == "__main__":
    from aocd.models import Puzzle

    # Get puzzle details and set up input
    puzzle = Puzzle(year=2023, day=7)

    # Submitting answers
    puzzle.answer_a = part1(puzzle.input_data)
    puzzle.answer_b = part2(puzzle.input_data)
