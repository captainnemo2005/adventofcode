"""
After saving Christmas five years in a row, you've decided to take a vacation at a nice resort on a tropical island.
Surely, Christmas will go on without you.

The tropical island has its own currency and is entirely cash-only.
The gold coins used there have a little picture of a starfish; the locals just call them stars.
None of the currency exchanges seem to have heard of them, but somehow,
you'll need to find fifty of these coins by the time you arrive so you can pay the deposit on your room.

To save your vacation, you need to get all fifty stars by December 25th.
Collect stars by solving puzzles. Two puzzles will be made available on each day in the Advent calendar;
the second puzzle is unlocked when you complete the first. Each puzzle grants one star. Good luck!
Before you leave, the Elves in accounting just need you to fix your expense report (your puzzle input);
apparently, something isn't quite adding up.

Specifically, they need you to find the two entries that sum to 2020 and then multiply those two numbers together.
For example, suppose your expense report contained the following:

1721
979
366
299
675
1456

In this list, the two entries that sum to 2020 are 1721 and 299.
Multiplying them together produces 1721 * 299 = 514579, so the correct answer is 514579.

Of course, your expense report is much larger. Find the two entries that sum to 2020;
what do you get if you multiply them together?
"""
import logging as log

log.basicConfig(level=log.DEBUG, format="%(asctime)s %(message)s")


def read_file(filename: str = "../data/day1data.txt") -> list:
    with open(filename, "r") as f:
        lines = [int(line) for line in f.read().split("\n")]
    return lines


def part1(data):
    for number in data:
        if (2020 - number) in data:
            return (2020 - number) * number


def part2(vals):
    for i in range(len(vals)):
        for j in range(i, len(vals)):
            if (2020 - vals[i] - vals[j]) in vals:
                return vals[i] * vals[j] * (2020 - vals[i] - vals[j])


if __name__ == "__main__":
    log.info("Load data...")
    data = read_file()
    log.info(f"Part 1: {part1(data)}")
    log.info(f"Part 2: {part2(data)}")
