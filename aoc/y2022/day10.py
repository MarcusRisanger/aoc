def eval_input(input_data: str):
    cycle = 0
    reg = 1

    for row in input_data.splitlines():
        if row == "noop":
            cycle += 1
            yield cycle, reg
        else:
            for _ in range(2):
                cycle += 1
                yield cycle, reg
            reg += int(row.split()[1])


def part1(input_data: str):

    strength = 0

    for cycle, reg in eval_input(input_data):
        if cycle % 40 == 20:
            strength += cycle * reg

    return strength


def part2(input_data):
    img: list[list[str]] = []
    for cycle, reg in eval_input(input_data):
        if (cycle - 1) % 40 == 0:
            img.append([])
        if reg - 1 <= ((cycle - 1) % 40) <= reg + 1:
            img[-1].append("#")
        else:
            img[-1].append(".")
    for row in img:
        print("".join(row).replace(".", " "))
    return img


if __name__ == "__main__":
    from aocd.models import Puzzle

    puzzle = Puzzle(2022, 10)

    puzzle.answer_a = part1(puzzle.input_data)
    part2(puzzle.input_data)
