def clean_input(inp: str) -> tuple[int, ...]:
    return tuple(map(int, inp.split("-")))


def check_valid(n: int, p2: bool = False) -> bool:
    nums = list(map(int, str(n)))
    if p2:
        return nums == sorted(nums) and any(nums.count(num) == 2 for num in set(nums))
    return nums == sorted(nums) and len(set(nums)) < len(nums)


assert check_valid(111111) is True
assert check_valid(223450) is False
assert check_valid(123789) is False

assert check_valid(112233, p2=True) is True
assert check_valid(123444, p2=True) is False
assert check_valid(111122, p2=True) is True


def part1(min: int, max: int) -> str:
    return str(sum(check_valid(n) for n in range(min, max + 1)))


def part2(min: int, max: int) -> str:
    return str(sum(check_valid(n, True) for n in range(min, max + 1)))


if __name__ == "__main__":
    from aocd.models import Puzzle

    # Get puzzle details and set up input
    puzzle = Puzzle(year=2019, day=4)

    min, max = clean_input(puzzle.input_data)

    # Submit answers
    puzzle.answer_a = part1(min, max)
    puzzle.answer_b = part2(min, max)
