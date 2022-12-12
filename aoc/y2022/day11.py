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

import re
from collections import defaultdict


class Monkey:
    def __init__(
        self, items: str, operation: callable, mod: int, to_true: int, to_false: int
    ) -> None:
        self.items: list[int] = list(map(int, [i for i in items.split(", ")]))
        self.operation = operation
        self.mod = mod
        self.to_true = to_true
        self.to_false = to_false


monkeys = defaultdict(dict)
pat = r".*(\d).*\n.*: (.*)\n.*=\s(.*)\n\D*(\d+)\n\D*(\d+)\n\D*(\d+)"
for row in test_data.split("\n\n")[:1]:
    monkey, items, op, mod, t, f = re.findall(pat, row)[0]
    monkeys[monkey]["items"] = list(map(int, [i for i in items.split(", ")]))
    monkeys[monkey]["operation"] = lambda old: eval(op)
    monkeys[monkey]["mod"] = mod
    # monkeys[monkey][]


a = monkeys[0]
