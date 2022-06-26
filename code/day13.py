"""
Inputs:

6,10
0,14
9,10
0,3
10,4
4,11
6,0
6,12
4,1
0,13
10,12
3,4
3,0
8,4
1,10
2,14
8,10
9,0

fold along y=7
fold along x=5

Outputs:
#####
#...#
#...#
#...#
#####
.....
.....
"""
import logging as log

log.basicConfig(level=log.DEBUG, format="%(asctime)s %(message)s")


def read_file():
    with open("../data/day13data.txt", "r") as file:
        lines = file.read().splitlines()

        max_x, max_y = 0, 0
        folds = []

        for line in lines:
            if 'fold' in line:
                folds.append(line.split()[-1].split('='))
            elif len(line) > 0:
                x,y = line.split(',')
                if int(x) > max_x:
                    max_x = int(x)
                if int(y) > max_y:
                    max_y = int(y)

        grid = [[' '] * (max_x + 1) for _ in range((max_y+1))]

        for line in lines:
            if (len(line)>0) and ('fold' not in line):
                y, x = line.split(',')

                grid[int(x)][int(y)] = '#'
        return folds,grid

def part1(folds,grid):
    point = 0
    val = int(folds[0][1])
    if folds[0][0] == 'y':
        for i in range(val):
            for j in range(len(grid[0])):
                if grid[i][j] == '#' or grid[2*val - i][j] == '#':
                    point += 1
    else:
        for i in range(len(grid)):
            for j in range(val):
                if grid[i][j] == '#' or grid[i][2*val - j] == '#':
                    point += 1
    return point

def part2(folds,grid):
    with open('../data/day13data.txt') as f:
        lines = f.read().splitlines()

    grid = [[' '] * 2000 for _ in range(2000)]
    folds = []

    for line in lines:
        if 'fold' in line:
            folds.append(line.split()[-1].split('='))
        elif len(line) > 0:
            x, y = line.split(',')
            grid[int(x)][int(y)] = '#'

    for f in folds:
        val = int(f[1])
        if f[0] == 'x':
            for i in range(val):
                for a in range(2000):
                    if grid[i][a] == '#' or grid[2 * val - i][a] == '#':
                        grid[i][a] = '#'
        else:
            for i in range(2000):
                for a in range(val):
                    if grid[i][a] == '#' or grid[i][2 * val - a] == '#':
                        grid[i][a] = '#'

    for i in range(40):
        print(''.join(grid[i][:6][::-1]))
if __name__ == "__main__":
    folds, grid = read_file()
    log.info(f"Part 1: {part1(folds,grid)}")
    log.info(f"Part 2: {part2(folds,grid)}")
