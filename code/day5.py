import pandas as pd
import numpy as np


def read_file() -> list:
    with open("../data/day5data.txt", "r") as file:
        lines = [line for line in file.read().split("\n")]
    data = []
    for line in lines:
        data.append(
            [int(x) for x in line.split("->")[0].split(",")]
            + [int(x) for x in line.split("->")[1].split(",")]
        )
    return data


def find_part_1(data, vents_map):

    print(np.count_nonzero(vents_map >= 2))


if __name__ == "__main__":
    data = pd.DataFrame(read_file(), columns=["x1", "y1", "x2", "y2"])
    data = data.query("x1 == x2" or "y1 == y2")
    data.reset_index(inplace=True, drop=True)
    max_value = max(
        data["x1"].max(), data["x2"].max(), data["y1"].max(), data["y2"].max()
    )
    vents_map = np.zeros((max_value, max_value))
    find_part_1(data, vents_map)
