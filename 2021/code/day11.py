"""
The energy level of each octopus is a value between 0 and 9. Here, the top-left octopus has an energy level of 5,
the bottom-right one has an energy level of 6, and so on.

You can model the energy levels and flashes of light in steps. During a single step, the following occurs:

First, the energy level of each octopus increases by 1.
Then, any octopus with an energy level greater than 9 flashes. This increases the energy level of all adjacent octopuses by 1,
including octopuses that are diagonally adjacent. If this causes an octopus to have an energy level greater than 9, it also flashes.
This process continues as long as new octopuses keep having their energy level increased beyond 9. (An octopus can only flash at most once per step.)
Finally, any octopus that flashed during this step has its energy level set to 0, as it used all of its energy to flash.

"""
import logging as log

log.basicConfig(level=log.DEBUG, format="%(asctime)s %(message)s")


def read_data() -> list:
    with open("../data/day11data.txt", "r") as file:
        lines = file.read().splitlines()
        return [[int(c) for c in line] for line in lines]


def part1(vals) -> int:
    flashes = 0
    for step in range(100):
        # log.info("Increase all octopuses by 1... ")
        for i in range(len(vals)):
            for j in range(len(vals[0])):
                vals[i][j] += 1
        change = True
        # log.info("Create the flash matrix for each octopus...")
        flashed = [[False] * len(vals[0]) for _ in range(len(vals))]

        while change:
            change = False
            for i in range(len(vals)):
                for j in range(len(vals[0])):
                    if vals[i][j] > 9 and not flashed[i][j]:
                        flashed[i][j] = True
                        change = True
                        for k in range(-1, 2):
                            for m in range(-1, 2):
                                newi = i + k
                                newj = j + m
                                if (
                                    0 <= newi
                                    and newi < len(vals)
                                    and 0 <= newj
                                    and newj < len(vals[0])
                                ):
                                    vals[newi][newj] += 1

        for i in range(len(vals)):
            for j in range(len(vals[0])):
                if flashed[i][j]:
                    flashes += 1
                    vals[i][j] = 0

    return flashes


def part2(vals) -> int:
    for step in range(10000):
        flashes = 0

        for i in range(len(vals)):
            for j in range(len(vals[0])):
                vals[i][j] += 1

        change = True
        flashed = [[False] * len(vals[0]) for _ in range(len(vals))]
        while change:
            change = False
            for i in range(len(vals)):
                for j in range(len(vals[0])):
                    if vals[i][j] > 9 and not flashed[i][j]:
                        flashed[i][j] = True
                        change = True
                        for k in range(-1, 2):
                            for m in range(-1, 2):
                                newi = i + k
                                newj = j + m
                                if (
                                    0 <= newi
                                    and newi < len(vals)
                                    and 0 <= newj
                                    and newj < len(vals[0])
                                ):
                                    vals[newi][newj] += 1

        for i in range(len(vals)):
            for j in range(len(vals[0])):
                if flashed[i][j]:
                    flashes += 1
                    vals[i][j] = 0

        if flashes == 100:
            return step + 1


if __name__ == "__main__":
    log.info(f"Read data ....")
    log.info(f"Part 1 = {part1(read_data())}")
    log.info(f"Part 2 = {part2(read_data())}")
