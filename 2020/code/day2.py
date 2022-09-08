"""
--- Day 2: Password Philosophy ---
Your flight departs in a few days from the coastal airport; the easiest way down to the coast from here is via toboggan.
The shopkeeper at the North Pole Toboggan Rental Shop is having a bad day.
"Something's wrong with our computers; we can't log in!" You ask if you can take a look.

Their password database seems to be a little corrupted: some of the passwords wouldn't have been allowed by the Official
 Toboggan Corporate Policy that was in effect when they were chosen.

To try to debug the problem, they have created a list (your puzzle input) of passwords
(according to the corrupted database) and the corporate policy when that password was set.

For example, suppose you have the following list:

1-3 a: abcde
1-3 b: cdefg
2-9 c: ccccccccc
Each line gives the password policy and then the password. The password policy indicates the lowest and
highest number of times a given letter must appear for the password to be valid.
For example, 1-3 a means that the password must contain a at least 1 time and at most 3 times.

In the above example, 2 passwords are valid. The middle password, cdefg, is not; it contains no instances of b,
but needs at least 1. The first and third passwords are valid: they contain one a or nine c, both within the limits of their respective policies.

How many passwords are valid according to their policies?
"""
import logging as log
import pandas as pd

log.basicConfig(level=log.DEBUG, format="%(asctime)s %(message)s")


def read_data():
    with open("../data/day2data.txt", "r") as f:
        lines = [line for line in f.read().split("\n")]
    x = [line.split(" ") for line in lines]
    return x


def part1(data):
    valid_password = 0
    for i in range(len(data)):
        if (data[i][2].count(data[i][1][0]) >= int(data[i][0].split("-")[0])) & (
            data[i][2].count(data[i][1][0]) <= int(data[i][0].split("-")[1])
        ):
            valid_password += 1
    return valid_password


def part2(data):
    valid_password = 0
    for i in range(len(data)):
        the_string = data[i][2]
        loc_1 = int(data[i][0].split("-")[0])
        loc_2 = int(data[i][0].split("-")[1])
        char = data[i][1][0]
        if ((the_string[loc_1 - 1] == char) & (the_string[loc_2 - 1] != char)) | (
            (the_string[loc_1 - 1] != char) & (the_string[loc_2 - 1] == char)
        ):
            # log.info(loc_1)
            # log.info(loc_2)
            # log.info(the_string)
            # log.info(char)
            valid_password += 1
    return valid_password


if __name__ == "__main__":
    data = read_data()
    log.info(f"Part 1: {part1(data)}")
    log.info(f"Part 1: {part2(data)}")
