def clean_input(input_data: str) -> dict[str, int]:
    instructions = input_data.splitlines()
    dirs = dict({"/": 0})
    current_dir: list[str] = []
    for row in instructions:
        if "cd .." in row:
            current_dir.pop()
        elif "$ cd" in row:
            current_dir.append(".".join(current_dir) + row.split()[-1])
        elif "$ ls" in row:
            pass
        else:
            s, n = row.split()
            if s == "dir":
                dir_name = ".".join(current_dir) + n
                dirs[dir_name] = 0
            else:
                for dir in current_dir:
                    dirs[dir] += int(s)
    return dirs


def part1(input_data: dict[str, int]) -> int:
    """Returns size dirs with a size of at most 100000"""
    return sum(v for v in input_data.values() if v <= 100000)


def part2(input_data: dict[str, int]) -> int:
    """Returns size of smallest dir that can be deleted to free up enough space"""
    return min(v for v in input_data.values() if v >= (-40000000 + input_data["/"]))


if __name__ == "__main__":
    from aocd.models import Puzzle

    # Get puzzle details and set up input
    puzzle = Puzzle(year=2022, day=7)
    input_data = clean_input(puzzle.input_data)

    # Submit answers
    puzzle.answer_a = part1(input_data)
    puzzle.answer_b = part2(input_data)
