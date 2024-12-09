Loc = int
Id = int
Addresses = list[Loc]
Empty = list[Addresses]
Files = dict[Id, Addresses]  # To make checksum easy


def clean_input(inp: str) -> tuple[Files, Addresses]:
    id = 0
    cursor = 0
    files = dict()
    addresses = list()
    for i, val in enumerate(inp):
        intval = int(val)
        locs = list(a + cursor for a in range(intval))
        if i % 2 == 0:
            files[id] = locs
            id += 1
        else:
            addresses.append(locs) if locs else None
        cursor += intval
    return files, addresses


def checksum(files: Files) -> int:
    return sum(sum(k * val for val in v) for k, v in files.items())


def defrag_bytes(files: Files, empty: Empty) -> Files:
    """For each file in reverse order, move bytes leftward to empty spaces."""
    files = files.copy()
    empty = [v for chunk in empty for v in chunk]  # Flatten chunks
    for file, addresses in sorted(files.items(), reverse=True):
        new_ad = [empty.pop(0) if ad > empty[0] else ad for ad in addresses[::-1]]
        files[file] = new_ad
    return files


def defrag_files(files: Files, empty: Empty) -> Files:
    """For each file in reverse order, move leftward to empty space that can fit the whole file."""
    files, empty = files.copy(), empty.copy()
    for file, addresses in sorted(files.items(), reverse=True):
        for i, chunk in enumerate(empty):
            if len(chunk) < len(addresses):
                continue  # check next chunk
            elif chunk[0] > addresses[0]:
                break  # Can't move left
            else:
                new_address, chunk = chunk[: len(addresses)], chunk[len(addresses) :]
                empty[i] = chunk
                files[file] = new_address
                break  # Moved file
    return files


def part1(files: Files, empty: Empty) -> int:
    files = defrag_bytes(files, empty)
    return checksum(files)


def part2(files: Files, empty: Empty) -> int:
    files = defrag_files(files, empty)
    return checksum(files)


if __name__ == "__main__":
    from aocd.models import Puzzle

    # Get puzzle details and set up input
    puzzle = Puzzle(year=2024, day=9)

    input_data = clean_input(puzzle.input_data)

    # Submit answers
    puzzle.answer_a = str(part1(*input_data))
    puzzle.answer_b = str(part2(*input_data))
