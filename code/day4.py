import pandas as pd
import numpy as np


def read_file() -> [list, list]:
    with open("../data/day4data.txt", "r") as f:
        lines = [line for line in f.read().split("\n")]
    draws = [int(x) for x in lines[0].split(",")]
    fields = []
    for i in range(2, len(lines), 6):
        cur_nums = []
        for j in range(5):
            cur_nums += [int(x) for x in lines[i + j].lstrip().strip().split()]
        fields.append(cur_nums)
    return draws, fields


def check_bingo(bingo: list, bingo_array: list):
    index_ = []

    for i in range(len(bingo_array)):
        index_.append([False] * 25)

    for i in range(len(bingo)):
        for j in range(len(bingo_array)):
            for k in range(len(bingo_array[j])):
                if bingo_array[j][k] == bingo[i]:
                    index_[j][k] = True
        for j in range(len(index_)):
            for a in range(5):
                if all(index_[j][a * 5 + k] for k in range(5)) or all(
                    index_[j][k * 5 + a] for k in range(5)
                ):
                    return cal_score(bingo[: i + 1], bingo_array[j], bingo[i])


def check_bingo_part2(bingo: list, bingo_array: list):
    index_ = []
    iswin = [False] * len(bingo_array)
    last_board = None

    for i in range(len(bingo_array)):
        index_.append([False] * 25)

    for i in range(len(bingo)):
        for j in range(len(bingo_array)):
            for k in range(len(bingo_array[j])):
                if bingo_array[j][k] == bingo[i]:
                    index_[j][k] = True
        for j in range(len(index_)):
            for a in range(5):
                if all(index_[j][a * 5 + k] for k in range(5)) or all(
                    index_[j][k * 5 + a] for k in range(5)
                ):
                    iswin[j] = True
                    if (False in iswin) == False:
                        return cal_score(bingo[: i + 1], bingo_array[j], bingo[i])


def cal_score(bingo_number: list, bingo_cards: list, last_number: int):
    print(last_number)
    print(sum(set(bingo_cards) - set(bingo_number)) * last_number)
    return sum(set(bingo_cards) - set(bingo_number)) * last_number


if __name__ == "__main__":
    bingo, bingo_array = read_file()
    check_bingo(bingo, bingo_array)
    check_bingo_part2(bingo, bingo_array)
