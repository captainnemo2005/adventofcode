"""
2199943210
3987894921
9856789892
8767896789
9899965678

Each number corresponds to the height of a particular location,
where 9 is the highest and 0 is the lowest a location can be.

Your first goal is to find the low points - the locations that are lower than any of its adjacent locations.
Most locations have four adjacent locations (up, down, left, and right);
locations on the edge or corner of the map have three or two adjacent locations, respectively.
(Diagonal locations do not count as adjacent.)

In the above example, there are four low points, all highlighted: two are in the first row (a 1 and a 0),
one is in the third row (a 5), and one is in the bottom row (also a 5).
All other locations on the heightmap have some lower adjacent location, and so are not low points.

The risk level of a low point is 1 plus its height.
In the above example, the risk levels of the low points are 2, 1, 6, and 6.
The sum of the risk levels of all low points in the heightmap is therefore 15.
"""
from functools import reduce
from itertools import product
from operator import mul
import numpy as np


def read_data() -> list:
    with open(
        "/2021/data/day9data.txt",
        "r",
    ) as file:
        pars_line = lambda line: [int(n) for n in line]
        return list(map(pars_line, file.read().splitlines()))


def part1(vals: list) -> int:
    low_points = []
    for x, y in product(range(len(vals[0])), range(len(vals))):
        is_low = True
        for xdiff, ydiff in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            x2, y2 = x + xdiff, y + ydiff
            if x2 >= 0 and y2 >= 0 and x2 < len(vals[0]) and y2 < len(vals):
                if vals[y2][x2] <= vals[y][x]:
                    is_low = False
                    break
        if is_low:
            low_points.append(vals[y][x])
    return sum(np.array(low_points) + 1)


def part2(vals: list) -> int:
    low_points: list[tuple[tuple[int, int], int]] = []
    for x, y in product(range(len(vals[0])), range(len(vals))):
        is_low = True
        for xdiff, ydiff in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            x2, y2 = x + xdiff, y + ydiff
            if x2 >= 0 and y2 >= 0 and x2 < len(vals[0]) and y2 < len(vals):
                if vals[y2][x2] <= vals[y][x]:
                    is_low = False
                    break
        if is_low:
            low_points.append(((x, y), vals[y][x]))

    basins: list[list[tuple[int, int]]] = []

    for low_point, _ in low_points:
        basin = {low_point}
        to_search = {low_point}
        while len(to_search) > 0:
            x, y = to_search.pop()
            for xdiff, ydiff in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                x2, y2 = x + xdiff, y + ydiff
                if x2 >= 0 and y2 >= 0 and x2 < len(vals[0]) and y2 < len(vals):
                    if 9 > vals[y2][x2] >= vals[y][x]:
                        if (x2, y2) not in basin:
                            basin.add((x2, y2))
                            to_search.add((x2, y2))
        basins.append(basin)
    # print(basins)
    largest_basins = sorted(map(len, basins), reverse=True)
    return reduce(
        mul,
        largest_basins[:3],
    )


if __name__ == "__main__":
    vals = read_data()
    print(f"Part 1: {part1(vals)}")
    print(f"Part 2: {part2(vals)}")
