import pandas as pd
import numpy as np


def read_file() -> list:
    with open(
        "/2021/data/day5data.txt",
        "r",
    ) as file:
        lines = [line.split(" -> ") for line in file.read().strip().split("\n")]
    return [
        [(int(s[0]), int(s[1])) for s in (x.split(",") for x in line)] for line in lines
    ]


def count_crossings(coords: list, allow_diagonoal: bool = False) -> int:
    segments = dict()
    for coord in coords:
        x1, x2, y1, y2 = coord[0][0], coord[1][0], coord[0][1], coord[1][1]
        x_dir = 1 if x1 < x2 else -1 if x1 > x2 else 0
        y_dir = 1 if y1 < y2 else -1 if y1 > y2 else 0
        dist = max(abs(x2 - x1), abs(y2 - y1))
        cond = True if allow_diagonoal else (x_dir == 0 or y_dir == 0)
        tmp = [(x1 + n * x_dir, y1 + n * y_dir) for n in range(dist + 1) if cond]
        for segment in tmp:
            if segment not in segments:
                segments[segment] = 1
            else:
                segments[segment] += 1
    return sum(1 for x in segments if segments[x] > 1)


def part1(coords: list) -> int:
    return count_crossings(coords)


def part2(coords: list) -> int:
    return count_crossings(coords, True)


if __name__ == "__main__":
    coords = read_file()
    print(f"Part 1: {part1(coords)}")
    print(f"Part 2: {part2(coords)}")
