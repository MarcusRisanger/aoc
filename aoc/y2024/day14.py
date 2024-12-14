from dataclasses import dataclass
from re import findall
from math import prod
from statistics import variance

Coord = tuple[int, int]
Heading = Coord
Variance = float

W = 101
H = 103


@dataclass
class Robot:
    x: int
    y: int
    vx: int
    vy: int

    def move(self) -> None:
        self.x, self.y = (self.x + self.vx) % W, (self.y + self.vy) % H


@dataclass
class Swarm:
    robots: list[Robot]
    time: int = 0

    def move(self):
        for r in self.robots:
            r.move()
        self.time += 1

    def safety_score(self):
        quadrants = (
            ((0, W // 2 - 1), (0, H // 2 - 1)),
            ((W // 2 + 1, W - 1), (0, H // 2 - 1)),
            ((0, W // 2 - 1), (H // 2 + 1, H - 1)),
            ((W // 2 + 1, W - 1), (H // 2 + 1, H - 1)),
        )
        return prod(
            sum(1 for robot in self.robots if (x[0] <= robot.x <= x[1]) and (y[0] <= robot.y <= y[1]))
            for x, y in quadrants
        )

    @property
    def variances(self) -> tuple[Variance, Variance]:
        return variance(robot.x for robot in self.robots), variance(robot.y for robot in self.robots)


def clean_input(inp: str) -> Swarm:
    return Swarm([Robot(*map(int, bot)) for bot in findall(r"(?:p=(\d+),(\d+) v=(-?\d+),(-?\d+))+", inp)])


def parts(swarm: Swarm) -> int:
    # Establish variances
    var_x = set()
    var_y = set()
    for _ in range(W * H):
        v_x, v_y = swarm.variances
        var_x.add(v_x)
        var_y.add(v_y)
        swarm.move()

        if swarm.time == 100:
            score = swarm.safety_score()

    # Set cutoffs
    coefficient = 1.1
    x_cutoff = sorted(var_x)[0] * coefficient
    y_cutoff = sorted(var_y)[0] * coefficient

    # Loop some more, lol
    for i in range(W * H):
        v_x, v_y = swarm.variances
        if v_x < x_cutoff and v_y < y_cutoff:
            return score, i
        swarm.move()


if __name__ == "__main__":
    from aocd.models import Puzzle

    # Get puzzle details and set up input
    puzzle = Puzzle(year=2024, day=14)

    input_data = clean_input(puzzle.input_data)

    # Submit answers
    puzzle.answer_a, puzzle.answer_b = parts(input_data)
