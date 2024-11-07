from aoc.y2021.day4 import clean_input, solve_board, part1, part2
from aocd.models import Puzzle

test_input = """7,4,9,5,11,17,23,2,0,14,21,24,10,16,13,6,15,25,12,22,18,20,8,19,3,26,1

22 13 17 11  0
 8  2 23  4 24
21  9 14 16  7
 6 10  3 18  5
 1 12 20 15 19

 3 15  0  2 22
 9 18 13 17  5
19  8  7 25 23
20 11 10 24  4
14 21 16 12  6

14 21 17 24  4
10 16 15  9 19
18  8 23 26 20
22 11 13  6  5
 2  0 12  3  7"""

actual_data = clean_input(Puzzle(2021, 4).input_data)


def test_clean_input():
    draws, boards = clean_input(test_input)
    assert draws[:4] == [7, 4, 9, 5]
    assert boards[0][22] == "00"
    assert boards[1][17] == "13"
    assert boards[2][16] == "11"
    assert solve_board(draws, boards[2]) == (11, 4512)
    assert solve_board(draws, boards[1]) == (14, 1924)


def test_part1():
    draws, boards = clean_input(test_input)
    assert part1(draws=draws, boards=boards) == 4512
    assert part1(*actual_data) == 29440


def test_part2():
    draws, boards = clean_input(test_input)
    assert part2(draws=draws, boards=boards) == 1924
    assert part2(*actual_data) == 13884
