"""
Suddenly, a swarm of crabs (each in its own tiny submarine - it's too deep for them otherwise) zooms in to rescue you!
They seem to be preparing to blast a hole in the ocean floor; sensors indicate a massive underground cave system just beyond where they're aiming!

The crab submarines all need to be aligned before they'll have enough power to blast a large enough hole for your submarine to get through.
However, it doesn't look like they'll be aligned before the whale catches you! Maybe you can help?

There's one major catch - crab submarines can only move horizontally.

You quickly make a list of the horizontal position of each crab (your puzzle input).
Crab submarines have limited fuel, so you need to find a way to make all of their horizontal positions match while requiring them to spend as little fuel as possible.
"""
import numpy as np

def read_data() -> list:
    with open(
            "/Users/cptnemo2005/Desktop/Work/self-sufficient-me/adventofcode/data/day7data.txt",
            "r",
    ) as file:
        line = file.read().strip().split("\n")[0].split(",")
    return [int(x) for x in line]

def calc_fuel(crab_horizontal : list, consecutive_sum: bool = False) -> int:
    unique = set(crab_horizontal)
    crab_horizontal_arr = np.array(crab_horizontal)
    optimal = []
    for i in range(0,max(unique)):
        x = abs(crab_horizontal_arr - i)
        if consecutive_sum:
            sum_ = 0
            for j in range(len(x)):
                sum_ += x[j]*(x[j]+1)/2
            optimal.append(sum_)
        else:
            optimal.append(sum(x))

    return min(optimal)

def part1(crab_horizontal : list) -> int:
    return calc_fuel(crab_horizontal)

def part2(crab_horizontal : list) -> int:
    return calc_fuel(crab_horizontal,True)
if __name__=='__main__':
    crabs_horizontal = read_data()
    print(f"Part 1: {part1(crabs_horizontal)}")
    print(f"Part 2: {part2(crabs_horizontal)}")