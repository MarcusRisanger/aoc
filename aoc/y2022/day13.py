def process_row(l: list | int, r: list | int):

    # If both inputs are ints, go for comparison
    if isinstance(l, int) and isinstance(r, int):
        if l < r:
            return 1
        if l > r:
            return -1
    # If one input is list, recursively call process
    if isinstance(l, list) and isinstance(r, int):
        return process_row(l, [r])
    if isinstance(l, int) and isinstance(r, list):
        return process_row([l], r)

    # If both inputs are lists, process each element recursively
    if isinstance(l, list) and isinstance(r, list):
        for x in map(process_row, l, r):
            if x:
                return x
        # If no result is found, the iterators are exhausted, check length
        return process_row(len(l), len(r))


def part1(input_data: str):
    return sum(
        i
        for i, row in enumerate(input_data, 1)
        if process_row(*map(eval, row.split())) == 1
    )


def part2(input_data: str):
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
    return (sort_sigs.index("[[2]]") + 1) * (sort_sigs.index("[[6]]") + 1)


if __name__ == "__main__":
    from aocd.models import Puzzle

    puzzle = Puzzle(2022, 13)
    input_data = puzzle.input_data.split("\n\n")

    puzzle.answer_a = part1(input_data)
    puzzle.answer_b = part2(input_data)
