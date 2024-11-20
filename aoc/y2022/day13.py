def process_row(left: list | int, right: list | int):
    # If both inputs are ints, go for comparison
    if isinstance(left, int) and isinstance(right, int):
        if left < right:
            return 1
        if left > right:
            return -1
    # If one input is list, recursively call process
    if isinstance(left, list) and isinstance(right, int):
        return process_row(left, [right])
    if isinstance(left, int) and isinstance(right, list):
        return process_row([left], right)

    # If both inputs are lists, process each element recursively
    if isinstance(left, list) and isinstance(right, list):
        for x in map(process_row, left, right):
            if x:
                return x
        # If no result is found, the iterators are exhausted, check length
        return process_row(len(left), len(right))


def part1(input_data: list[str]) -> str:
    return str(
        sum(
            i
            for i, row in enumerate(input_data, 1)
            if process_row(*map(eval, row.split())) == 1
        )
    )


def part2(input_data: list[str]) -> str:
    signals = [item for sublist in input_data for item in sublist.split()]
    sort_sigs = ["[[2]]", "[[6]]"]  # Adding key signals
    for sig in signals:
        # Create shallow copy to avoid expanding enumeration per iteration
        for i, s in enumerate(sort_sigs.copy()):
            # Insert new signal where it encounters the first sorted
            # signal of a lower order than the new signal.
            if process_row(eval(sig), eval(s)) == 1:
                sort_sigs.insert(i, sig)
                break
        # If no higher order was found, append
        sort_sigs.append(sig)
    return str((sort_sigs.index("[[2]]") + 1) * (sort_sigs.index("[[6]]") + 1))


if __name__ == "__main__":
    from aocd.models import Puzzle

    puzzle = Puzzle(2022, 13)
    input_data = puzzle.input_data.split("\n\n")

    puzzle.answer_a = part1(input_data)
    puzzle.answer_b = part2(input_data)
