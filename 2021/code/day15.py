"""
Inputs:

1163751742
1381373672
2136511328
3694931569
7463417111
1319128137
1359912421
3125421639
1293138521
2311944581

Outputs:

The total risk of this path is 40 (the starting position is never entered, so its risk is not counted).
"""
import logging as log

log.basicConfig(level=log.DEBUG, format="%(asctime)s %(message)s")

from queue import PriorityQueue


def read_file() -> tuple:
    with open(f"../data/day15data.txt", "r") as f:
        lines = f.read().splitlines()
    data = list()
    for line in lines:
        data += [int(x) for x in line]
    return len(lines[0]), data


def get_neighbors(dim: int) -> dict:
    neighbors = dict()
    for y in range(dim):
        for x in range(dim):
            neighbors[x + y * dim] = [
                x + d[0] + (y + d[1]) * dim
                for d in ((-1, 0), (1, 0), (0, -1), (0, 1))
                if 0 <= x + d[0] < dim and 0 <= y + d[1] < dim
            ]
    return neighbors


def dijkstra(cavern: tuple) -> dict:
    dimension, graph = cavern[0], cavern[1]
    neighbors = get_neighbors(dimension)
    queue = PriorityQueue()
    queue.put((0, 0))
    dist = {0: 0}

    while not queue.empty():
        distance, idx = queue.get()
        for neighbor in neighbors[idx]:
            d = distance + graph[neighbor]
            if neighbor not in dist or dist[neighbor] > d:
                dist[neighbor] = d
                queue.put((d, neighbor))
    return dist


def expand(cavern: tuple) -> tuple:
    dim = cavern[0]
    # expand to the right
    tmp = list()
    for y in range(dim):
        for i in range(5):
            for x in range(dim):
                val = cavern[1][x + y * dim] + i
                if val > 9:
                    val -= 9
                tmp.append(val)
    cave = tmp

    # expand to the bottom
    for _ in range(4):
        tmp = [n + 1 if n + 1 < 10 else n - 8 for n in tmp]
        cave += tmp

    return dim * 5, cave


def part1(cavern: tuple) -> int:
    return dijkstra(cavern)[cavern[0] ** 2 - 1]


def part2(cavern: tuple) -> int:
    cavern = expand(cavern)
    return dijkstra(cavern)[cavern[0] ** 2 - 1]


if __name__ == "__main__":
    vals = read_file()
    print(f"Part 1: {part1(vals)}")
    print(f"Part 2: {part2(vals)}")
