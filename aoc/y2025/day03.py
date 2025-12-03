def joltage(inp: str, length: int = 2) -> int:
    max_joltage = ""
    start = 0  # We start from beginning of string
    for i in range(length, 0, -1):  # 12, 11, 10 etc.
        # Set end for search to ensure that enough batteries are left after
        end = len(inp) - i + 1

        # Now we find the highest integer from current starting point to end
        # point, and add this to max_joltage var
        # We don't have to cast, just sort by int type as key in the function
        max_val = max((i for i in inp[start:end]), key=int)
        max_joltage += max_val

        # For the next digit, we have to start our search from
        # after the first occurrence of the max value
        # increment start point with first index in current slice
        # where max_val is found, but add 1 to avoid picking the
        # same value many times
        start += inp[start:].find(max_val) + 1

    return int(max_joltage)


def part1(inp: str) -> int:
    return sum(joltage(row) for row in inp.splitlines())


def part2(inp: str) -> int:
    return sum(joltage(row, 12) for row in inp.splitlines())


if __name__ == "__main__":
    from aocd.models import Puzzle

    # Get puzzle details and set up input
    puzzle = Puzzle(year=2025, day=3)
    input_data = puzzle.input_data

    # Submit answers
    puzzle.answer_a = str(part1(input_data))
    puzzle.answer_b = str(part2(input_data))
