"""
Fish span 1 every 7 days
Although you know nothing about this specific species of lanternfish,
you make some guesses about their attributes. Surely, each lanternfish creates a new lanternfish once every 7 days.

However, this process isn't necessarily synchronized between every lanternfish -
one lanternfish might have 2 days left until it creates another lanternfish, while another might have 4.
So, you can model each fish as a single number that represents the number of days until it creates a new lanternfish.

Furthermore, you reason, a new lanternfish would surely need slightly longer before it's capable of producing more lanternfish: two more days for its first cycle.

"""

import numpy as np


def read_data() -> list:
    with open(
        "/Users/cptnemo2005/Desktop/Work/self-sufficient-me/adventofcode/data/day6data.txt",
        "r",
    ) as file:
        line = file.read().strip().split("\n")[0].split(",")
    return [int(x) for x in line]


def part1(fishes: list, day: int) -> int:
    print("Initial state: ",fishes)
    for i in range(0, day):
        for j in range(len(fishes)):
            if fishes[j] == 0:
                fishes[j] = 6
                fishes.append(8)
            else:
                fishes[j] -= 1
        # if i == 0:
        #     print("After day ", i+1, " day: ",fishes)
        # else:
        #     print("After day ", i + 1, " days: ",fishes)
        print(len(fishes))
    return len(fishes)

def part2(fishes: list, day: int)-> int:
    fishes_ = [fishes.count(x) for x in range(9)]
    for i in range(day):
        new_fishes = fishes_[0]
        fishes_ = fishes_[1:] + [new_fishes]
        fishes_[6] += new_fishes
        print("Day ", i , " fishes = ", sum(fishes_))
    return sum(fishes_)
if __name__ == "__main__":
    fishes = read_data()
    print(f"Part 1: {part1(fishes,80)}")
    print(f"Part 2: {part2(fishes,256)}")
