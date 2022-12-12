import re
from math import prod


class Monkey:
    def __init__(
        self,
        monkey: str,
        items: str,
        operation: callable,
        mod: str,
        to_true: str,
        to_false: str,
    ) -> None:
        self.name: str = monkey
        self.items: list[int] = list(map(int, [i for i in items.split(", ")]))
        self.operation: callable = lambda old: eval(operation)
        self.mod: int = int(mod)
        self.to_true: int = int(to_true)
        self.to_false: int = int(to_false)
        self.inspected = 0

    def inspect_items(self, part1: bool = True, common_mod: int = None):
        to_true = []
        to_false = []
        while self.items:
            self.inspected += 1
            if part1:
                i = self.operation(self.items.pop(0)) // 3
            else:
                i = self.operation(self.items.pop(0)) % common_mod
            if i % self.mod == 0:
                to_true.append(i)
            else:
                to_false.append(i)
        return self.to_true, to_true, self.to_false, to_false


class MonkeyBusiness:
    def __init__(self, input_data: str) -> None:
        self.monkeys: list[Monkey] = []
        self.__parse_monkeys(input_data)
        self.common_mod = prod([i.mod for i in self.monkeys])

    def __parse_monkeys(self, input_data: str) -> None:
        pattern = r".*(\d).*\n.*: (.*)\n.*=\s(.*)\n\D*(\d+)\n\D*(\d+)\n\D*(\d+)"
        for row in input_data.split("\n\n"):
            monkey, items, op, mod, t, f = re.findall(pattern, row)[0]
            self.monkeys.append(
                Monkey(
                    monkey=f"Monkey {monkey}",
                    items=items,
                    operation=op,
                    mod=mod,
                    to_true=t,
                    to_false=f,
                )
            )

    def run(self, rounds: int, part1: bool = True):
        round = 1
        while True:
            for m in self.monkeys:
                tt, t, tf, f = m.inspect_items(part1, self.common_mod)
                self.monkeys[tt].items.extend(t)
                self.monkeys[tf].items.extend(f)

            if round == rounds:
                return prod(sorted([i.inspected for i in self.monkeys])[-2:])
            round += 1


if __name__ == "__main__":
    from aocd.models import Puzzle

    puzzle = Puzzle(2022, 11)
    input_data = puzzle.input_data
    mb = MonkeyBusiness(input_data)

    puzzle.answer_a = MonkeyBusiness(input_data).run(20)
    puzzle.answer_b = MonkeyBusiness(input_data).run(10_000, False)
