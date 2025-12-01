from dataclasses import dataclass

Coord = tuple[int, int]
Heading = Coord
Block = str
Moves = str
Move = str
Grid = dict[Coord, Block]


def next_coord(start: Coord, heading: Heading) -> Coord:
    return start[0] + heading[0], start[1] + heading[1]


directions: dict[Move, Heading] = {"^": (0, -1), "v": (0, 1), ">": (1, 0), "<": (-1, 0)}


@dataclass
class Box:
    at: list[Coord]

    def push(self, heading) -> None:
        self.at = [(c[0] + heading[0], c[1] + heading[1]) for c in self.at]

    def __hash__(self):
        return hash(tuple(sorted(self.at)))


@dataclass
class Warehouse:
    boxes: list[Box]
    walls: set[Coord]
    robot: Coord
    moves: str

    def do(self) -> int:
        for move in self.moves:
            self.move_robot(move)
        return self.gps_coord()

    def gps_coord(self) -> int:
        """Calculate GPS score."""
        return sum(box.at[0][0] + box.at[0][1] * 100 for box in self.boxes)

    def boxes_at(self, coord: Coord) -> set[Box]:
        """Return box that exists in coordinate."""
        return {b for b in self.boxes if coord in b.at}

    def wall_at(self, coord: Coord) -> bool:
        """Check if wall exists at coordinate."""
        return coord in self.walls

    def move_boxes(self, boxes: list[Box], heading: Heading) -> None:
        """Loop through boxes, add heading to coordinates."""
        for box in boxes:
            box.push(heading)

    def move_robot(self, move: str) -> None:
        """Moves robot and pushes boxes if possible."""
        heading = directions[move]
        move_to = next_coord(self.robot, heading)

        if self.wall_at(move_to):  # Obstruction, can't move
            return

        boxes = self.boxes_at(move_to)

        if not boxes:  # No obstruction, can move to next
            self.robot = move_to
            return

        pushing: set[Box] = set()
        walls = False
        while boxes:  # Obstruction, check if can move
            pushing.update(boxes)
            boxes = set.union(*[self.boxes_at(next_coord(c, heading)) for box in pushing for c in box.at])
            boxes = boxes.difference(pushing)
            walls = any(self.wall_at(next_coord(c, heading)) for box in pushing for c in box.at)
            if walls:
                break

        if walls:  # Don't move
            return

        self.move_boxes(pushing, heading)
        self.robot = move_to


def clean_input(inp: str, p2: bool = False) -> Warehouse:
    """Parse data into list of Regions using flood fill."""
    raw_c, raw_m = inp.split("\n\n")

    if p2:
        raw_c = raw_c.replace("#", "##")
        raw_c = raw_c.replace(".", "..")
        raw_c = raw_c.replace("@", "@.")
        raw_c = raw_c.replace("O", "[]")

    walls = set()
    boxes = list()
    robot = None
    moves = "".join(raw_m.splitlines())

    for y, row in enumerate(raw_c.splitlines()):
        for x, val in enumerate(row):
            if val == "@":
                robot = (x, y)
            elif val == "#":
                walls.add((x, y))
            elif val == "O":
                boxes.append(Box([(x, y)]))
            elif val == "[":
                boxes.append(Box([(x, y), (x + 1, y)]))

    return Warehouse(boxes, walls, robot, moves)


if __name__ == "__main__":
    from aocd.models import Puzzle

    # Get puzzle details and set up input
    puzzle = Puzzle(year=2024, day=15)

    # Submit answers
    puzzle.answer_a = clean_input(puzzle.input_data).do()
    puzzle.answer_b = clean_input(puzzle.input_data, True).do()
