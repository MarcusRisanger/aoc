from functools import partial


Mass = str
Orbiting = str
Orbits = dict[Mass, Orbiting]


def clean_input(inp: str) -> dict[Mass, Orbiting]:
    """Parses directly into child:parent dict."""
    return {b: a for row in inp.splitlines() for a, b in [row.split(")")]}


def count_orbits(mass: Mass, orbits: dict[Mass, Orbiting]) -> int:
    """Counts direct and indirect orbits for a given mass."""
    if mass not in orbits:
        return 0  # Doesn't orbit anything
    return 1 + count_orbits(orbits[mass], orbits)


def part1(orbits: Orbits) -> str:
    count = partial(count_orbits, orbits=orbits)
    return str(sum(count(m) for m in orbits.keys()))


def track_orbits(node: str, orbits: Orbits) -> Mass:
    """All orbits Node belongs to."""
    out = []
    while True:
        if node not in orbits:
            return out
        else:
            out.append(orbits[node])
            node = out[-1]


def part2(orbits: Orbits) -> str:
    orbits_you = track_orbits("YOU", orbits)
    orbits_san = track_orbits("SAN", orbits)
    for i, node in enumerate(orbits_you):
        if node in orbits_san:
            return str(orbits_san.index(node) + i)


if __name__ == "__main__":
    from aocd.models import Puzzle

    # Get puzzle details and set up input
    puzzle = Puzzle(year=2019, day=6)

    orbits = clean_input(puzzle.input_data)
    # Submit answers
    puzzle.answer_a = part1(orbits)
    puzzle.answer_b = part2(orbits)
