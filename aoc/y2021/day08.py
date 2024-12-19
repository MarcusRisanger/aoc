"""
AOC 2021, Day 8:
  - Part 1: Simple pattern matching
  - Part 2: More advanced pattern matching
"""


def clean_input(input_data: str) -> list[list[str]]:
    return [list(map(str.strip, row.split("|"))) for row in input_data.splitlines()]


def part1(data: list[list[str]]) -> int:
    """Returns count of digits 1, 4, 7, 8 in data."""
    lengths = [2, 4, 3, 7]
    counter = 0
    for _, outs in data:
        counter += sum(1 for digit in outs.split() if len(digit) in lengths)
    return counter


def part2(data: list[list[str]]) -> int:
    """Returns sum of each row's pattern matched code.
    Uses known masks to differentiate each digit in the display."""
    total = 0
    for signal, output in data:
        # Establishing length of each signal digit to establish our mask
        # len = 4 is display 4, len = 2 is display 1.
        s = {len(s): set(s) for s in signal.split()}
        n = ""
        for o in map(set, output.split()):
            # Iterating over each output digit to map actual value
            # Based on length and overlap with known "4" and known "1"
            match len(o), len(o & s[4]), len(o & s[2]):
                case 6, 3, 2:
                    n += "0"
                case 2, _, _:
                    n += "1"
                case 5, 2, 1:
                    n += "2"
                case 5, 3, 2:
                    n += "3"
                case 4, _, _:
                    n += "4"
                case 5, 3, 1:
                    n += "5"
                case 6, 3, 1:
                    n += "6"
                case 3, _, _:
                    n += "7"
                case 7, _, _:
                    n += "8"
                case 6, 4, 2:
                    n += "9"
        total += int(n)
    return total


if __name__ == "__main__":
    from aocd.models import Puzzle

    puzzle = Puzzle(year=2021, day=8)
    input_data = clean_input(puzzle.input_data)

    puzzle.answer_a = part1(input_data)
    puzzle.answer_b = part2(input_data)
