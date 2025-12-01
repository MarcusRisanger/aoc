from dataclasses import dataclass
import re

Velocity = int
Step = int
Steps = list[Step]
Viable = dict[Velocity, Steps]
MaxStep = Step


@dataclass
class Target:
    x_min: int
    x_max: int
    y_min: int
    y_max: int


def clean_input(inp: str) -> Target:
    return Target(*map(int, re.findall(r"(-?\d+)", inp)))


def cum_height(v) -> int:
    if v == 0:
        return 0
    return v + cum_height(v - 1)


def max_vyi(target: Target):
    """
    Get maximum initial vertical velocity.

    All velocities will cross through y=0 on the way down.
    Max vertical velocity is when the difference between lowest
    point in the target is hit in the following step, so the step size
    has to be one less than the difference between start and lowest target point.
    """
    diff = (0 - target.y_min) - 1  # The step
    return cum_height(diff)


def viable_vys(target: Target) -> tuple[Viable, MaxStep]:
    viable = dict()
    max_step = 0

    for vy in range(target.y_min, -target.y_min):
        step = 0
        v_curr, y_curr = vy, 0
        valid_steps = list()

        while True:
            if target.y_min <= y_curr <= target.y_max:
                valid_steps.append(step)
                max_step = max(max_step, step)

            y_curr += v_curr
            v_curr -= 1
            step += 1

            if y_curr < target.y_min:
                break

        if valid_steps:
            viable[vy] = valid_steps

    return viable, max_step


def viable_vxs(target: Target, max_step: int) -> Viable:
    viable = dict()
    for vx in range(target.x_max + 1):
        step = 0
        v_curr, x_curr = vx, 0
        valid_steps = list()
        while step <= max_step:
            if target.x_min <= x_curr <= target.x_max:
                valid_steps.append(step)
            elif x_curr < target.x_min and v_curr == 0:
                break

            x_curr += v_curr
            v_curr = 0 if v_curr == 0 else v_curr - 1
            step += 1

            if x_curr > target.x_max:
                break

        if valid_steps:
            viable[vx] = valid_steps
    return viable


def count_viable_combinations(target: Target) -> int:
    viable_y, max_step = viable_vys(target)
    viable_x = viable_vxs(target, max_step)

    return len([(x, y) for x, xs in viable_x.items() for y, ys in viable_y.items() if any(xx in ys for xx in xs)])


if __name__ == "__main__":
    from aocd.models import Puzzle

    puzzle = Puzzle(2021, 17)
    input_data = clean_input(puzzle.input_data)

    puzzle.answer_a = max_vyi(input_data)
    puzzle.answer_b = count_viable_combinations(input_data)
