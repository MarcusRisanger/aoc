from collections import defaultdict

Engraving = int
Count = int
Stones = dict[Engraving, Count]


def clean_input(inp: str) -> Stones:
    """Parse into stones."""
    stones: Stones = defaultdict(int)
    for i in map(int, inp.split()):
        stones[i] += 1
    return stones


def split(engraving: Engraving) -> tuple[Engraving, Engraving]:
    """Returns engravings for split stones."""
    string = str(engraving)
    return int(string[: len(string) // 2]), int(string[len(string) // 2 :])


def blink(stones: Stones) -> Stones:
    """Performs a blink."""
    new_stones: Stones = defaultdict(Count)
    for engraving, count in stones.items():
        if engraving == 0:  # Carry over to engraving 1
            new_stones[1] += count
        elif len(str(engraving)) % 2 == 0:  # Split stone
            for i in split(engraving):
                new_stones[i] += count
        else:  # Replace stone with n*2024
            new_stones[engraving * 2024] += count
    return new_stones


def do_the_blink(stones: Stones, blinks: int) -> int:
    """Performs.. many blinks. Returns final stone count."""
    for _ in range(blinks):
        stones = blink(stones)
    return sum(v for v in stones.values())


if __name__ == "__main__":
    from aocd.models import Puzzle

    # Get puzzle details and set up input
    puzzle = Puzzle(year=2024, day=11)

    input_data = clean_input(puzzle.input_data)

    # Submit answers
    puzzle.answer_a = str(do_the_blink(input_data, 25))
    puzzle.answer_b = str(do_the_blink(input_data, 75))
