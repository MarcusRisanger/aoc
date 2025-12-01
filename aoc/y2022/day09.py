from collections import defaultdict


def touching(hx, hy, tx, ty):
    touches = [
        (0, -1),
        (0, 0),
        (0, 1),
        (1, -1),
        (1, 0),
        (1, 1),
        (-1, -1),
        (-1, 0),
        (-1, 1),
    ]
    return (hx - tx, hy - ty) in touches


def move_head(hx: int, hy: int, direction: str) -> tuple[int, int]:
    move = {"D": (1, 0), "U": (-1, 0), "R": (0, 1), "L": (0, -1)}
    dx, dy = move[direction]
    return hx + dx, hy + dy


def move_tail(hx, hy, tx, ty):
    difx, dify = hx - tx, hy - ty
    if touching(hx, hy, tx, ty):
        return tx, ty
    elif difx and dify:
        return tx + (difx // abs(difx)), ty + (dify // abs(dify))
    else:
        return tx + ((difx) // 2), ty + ((dify) // 2)


def SNEK(input_data: str, length: int = 2) -> int:
    t_visit = defaultdict(int)
    snek = [(0, 0)] * length
    t_visit[snek[-1]] += 1
    for row in input_data.splitlines():
        d, i = row.split()
        for _ in range(int(i)):
            snek[0] = move_head(*snek[0], d)
            for i in range(1, len(snek)):
                snek[i] = move_tail(*snek[i - 1], *snek[i])
                t_visit[snek[-1]] += 1
    return len(t_visit)


if __name__ == "__main__":
    from aocd.models import Puzzle

    # Get puzzle details and set up input
    puzzle = Puzzle(year=2022, day=9)
    input_data = puzzle.input_data

    # Submit answers
    puzzle.answer_a = SNEK(input_data, 2)
    puzzle.answer_b = SNEK(input_data, 10)


# This solution by `u/4HbQ` using complex numbers as
# positional coordinates is ULTRA clean
#
# ///
#
# rope = [0] * 10
# seen = [set([x]) for x in rope]
# dirs = {'L':+1, 'R':-1, 'D':1j, 'U':-1j}
# sign = lambda x: complex((x.real>0) - (x.real<0), (x.imag>0) - (x.imag<0))

# for line in open('in.txt'):
#     d, n = line.split()

#     for _ in range(int(n)):
#         rope[0] += dirs[d]

#         for i in range(1, 10):
#             dist = rope[i-1] - rope[i]
#             if abs(dist) >= 2:
#                 rope[i] += sign(dist)
#                 seen[i].add(rope[i])

# print(len(seen[1]), len(seen[9]))
