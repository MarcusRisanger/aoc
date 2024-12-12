from dataclasses import dataclass

Coord = tuple[int, int]
Grid = dict[Coord, str]
Adjacent = Coord
Diagonal = Coord
Vertice = tuple[Adjacent, Adjacent, Diagonal]

N_4 = ((0, 1), (0, -1), (1, 0), (-1, 0))
TOP_LEFT: Vertice = ((-1, 0), (0, -1), (-1, -1))
TOP_RGHT: Vertice = ((1, 0), (0, -1), (1, -1))
BTM_LEFT: Vertice = ((-1, 0), (0, 1), (-1, 1))
BTM_RGHT: Vertice = ((1, 0), (0, 1), (1, 1))


@dataclass
class Region:
    coords: set[Coord]

    @property
    def area(self) -> int:
        return len(self.coords)

    @property
    def perimeter(self) -> int:
        return sum(4 - sum(self.get_neighbors(c)) for c in self.coords)

    def get_neighbors(self, coord: Coord, ns: tuple[Coord] = N_4) -> list[Coord]:
        """Return whether neighbors at given coords exist."""
        possible = [(coord[0] + n[0], coord[1] + n[1]) for n in ns]
        return [1 if n in self.coords else 0 for n in possible]

    def coord_sides(self, coord: Coord) -> int:
        """
        Check each diagonal vertice of a coord to check whether vertice represents a corner.

        Coord vertice is an outer corner if adjacent neighbors are not in Region.
        Coord vertice is an inner corner if adjacent neighbors are in Region, and diagonal neighbor is not.
        """
        corners = 0
        for vert in (TOP_LEFT, TOP_RGHT, BTM_LEFT, BTM_RGHT):
            ns = self.get_neighbors(coord, vert)
            corners += sum(ns[:2]) == 2 and ns[2] == 0  # Is inner corner
            corners += sum(ns[:2]) == 0  # Is outer corner

        return corners

    @property
    def sides(self) -> int:
        return sum(self.coord_sides(c) for c in self.coords)


def clean_input(inp: str) -> list[Region]:
    """Parse data into list of Regions using flood fill."""
    coords = {(x, y): val for y, row in enumerate(inp.splitlines()) for x, val in enumerate(row)}

    out: list[Region] = []
    assigned: set[Coord] = set()
    to_check = [k for k in coords]

    def get_neighbors(coord: Coord) -> set[Coord]:
        return {(coord[0] + n[0], coord[1] + n[1]) for n in ((0, 1), (0, -1), (1, 0), (-1, 0))}

    for start in to_check:
        if start in assigned:  # Coord belongs to another polygon
            continue
        current_polygon: set[Coord] = set()
        value = coords[start]
        frontier = {start}

        while frontier:
            current = frontier.pop()  # Get a coordinate
            current_polygon.add(current)  # Shove it into current polygon
            ns = {
                n for n in get_neighbors(current) if coords.get(n) == value and n not in current_polygon
            }  # Get valid neighbors
            frontier.update(ns)  # Update frontier with valid neighbors

        assigned.update(current_polygon)
        out.append(Region(current_polygon))

    return out


def part1(polygons: list[Region]) -> int:
    return sum(p.area * p.perimeter for p in polygons)


def part2(polygons: list[Region]) -> int:
    return sum(p.sides * p.area for p in polygons)


if __name__ == "__main__":
    from aocd.models import Puzzle

    # Get puzzle details and set up input
    puzzle = Puzzle(year=2024, day=12)

    input_data = clean_input(puzzle.input_data)

    # Submit answers
    puzzle.answer_a = str(part1(input_data))
    puzzle.answer_b = str(part2(input_data))
