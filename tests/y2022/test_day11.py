from aoc.y2022.day11 import MonkeyBusiness
from aocd.models import Puzzle


test_data = """Monkey 0:
  Starting items: 79, 98
  Operation: new = old * 19
  Test: divisible by 23
    If true: throw to monkey 2
    If false: throw to monkey 3

Monkey 1:
  Starting items: 54, 65, 75, 74
  Operation: new = old + 6
  Test: divisible by 19
    If true: throw to monkey 2
    If false: throw to monkey 0

Monkey 2:
  Starting items: 79, 60, 97
  Operation: new = old * old
  Test: divisible by 13
    If true: throw to monkey 1
    If false: throw to monkey 3

Monkey 3:
  Starting items: 74
  Operation: new = old + 3
  Test: divisible by 17
    If true: throw to monkey 0
    If false: throw to monkey 1"""

actual_data = Puzzle(2022, 11).input_data


def test_monkey_business():
    assert MonkeyBusiness(test_data).run(20) == 10605
    assert MonkeyBusiness(test_data).run(1_000, False) == 27019168
    assert MonkeyBusiness(test_data).run(2_000, False) == 108263829
    assert MonkeyBusiness(test_data).run(10_000, False) == 2713310158

    assert MonkeyBusiness(actual_data).run(20) == 90294
    assert MonkeyBusiness(actual_data).run(10_000, False) == 18170818354
