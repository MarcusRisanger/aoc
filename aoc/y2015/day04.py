from hashlib import md5


def find(inp: str, n: int) -> int:
    i = 0
    while True:
        if md5(bytes(f"{inp}{i}", "utf-8")).hexdigest().startswith("0" * n):
            return i
        i += 1


if __name__ == "__main__":
    from aocd.models import Puzzle

    # Get puzzle details and set up input
    puzzle = Puzzle(year=2015, day=4)

    # Submit answers
    puzzle.answer_a = str(find(puzzle.input_data, 5))
    puzzle.answer_b = str(find(puzzle.input_data, 6))
