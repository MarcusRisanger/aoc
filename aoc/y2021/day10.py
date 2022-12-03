"""
AOC 2021, Day 10:
   - Part 1: Check for valid brackets
   - Part 2: Again
"""


def syntax_error_score(input_data: str) -> tuple[int, int]:
    combos = {")": "(", "]": "[", "}": "{", ">": "<"}
    illegal_pts = {")": 3, "]": 57, "}": 1197, ">": 25137}
    add_pts = {"(": 1, "[": 2, "{": 3, "<": 4}
    points = 0
    scores = []

    for line in input_data.splitlines():
        elements = []
        skip = False
        for character in line:
            if character in combos.values():
                elements.append(character)
            elif elements.pop() != combos[character]:
                points += illegal_pts[character]
                skip = True
                break  # terminate loop on first hit
        if not skip:
            pts = 0
            for element in elements[::-1]:  # Reverse list!
                pts = pts * 5 + add_pts[element]
            scores.append(pts)

    return points, sorted(scores)[len(scores) // 2]


if __name__ == "__main__":
    from aocd.models import Puzzle

    puzzle = Puzzle(year=2021, day=10)

    puzzle.answer_a, puzzle.answer_b = syntax_error_score(puzzle.input_data)
