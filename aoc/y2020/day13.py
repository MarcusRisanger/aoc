from math import prod

ID = int
Time = int
Wait = int
Buses = dict[ID, Time]


def clean_input(inp: str) -> tuple[Time, Buses]:
    t, id = inp.splitlines()
    return int(t), {int(id): i for i, id in enumerate(id.split(",")) if id.isnumeric()}


def wait_for_next(id: ID, t: Time) -> Wait:
    """Time to wait for the given bus `id` (periodicity) at time `t`."""
    return 0 if t % id == 0 else id - (t % id)


def part1(t: Time, buses: Buses) -> str:
    """
    Calculate the waiting times per ID.

    The answer is the product of bus ID that will leave closest after `t`,
    multiplied with the number of minutes we have to wait.
    """
    waits = [(wait_for_next(id, t), id) for id in buses]
    earliest = min(waits, key=lambda x: x[0])
    return str(prod(earliest))


def part2(buses: Buses) -> str:
    """
    Calculate the first time step `t` from where all buses will leave
    at time `t + index(bus)`.

    We find the periodicity for a single bus first, then we increase
    step size by that bus ID to find the periodicity for buses 1+2.
    We loop through all the buses!
    """
    # We start at time 0 with steps of 1
    time = 0
    step = 1

    # We loop over all the buses
    for id in buses:
        # We check if the current time is good for this bus to leave
        # The time + offset determines if the current ID is scheduled
        while wait_for_next(id, time + buses[id]):
            # Move forward in time with the current step size
            time += step

        # When a bus can leave (wait_for_next == 0)
        # We increment the step size with the bus ID
        # If the bus can leave at step (time+bus offset) = X, it can also leave at step X + ID
        step *= id  # Incrementing the step by bus ID

    # When all buses are "harmonized", we can return the time.
    return str(time)


if __name__ == "__main__":
    from aocd.models import Puzzle

    puzzle = Puzzle(2020, 13)

    time, buses = clean_input(puzzle.input_data)

    puzzle.answer_a = part1(time, buses)
    puzzle.answer_b = part2(buses)
