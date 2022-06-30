"""
Ahead of you is what appears to be a large ocean trench. Could the keys have fallen into it? You'd better send a probe to investigate.

The probe launcher on your submarine can fire the probe with any integer velocity in the x (forward) and y (upward, or downward if negative) directions.
For example, an initial x,y velocity like 0,10 would fire the probe straight up, while an initial velocity like 10,
-1 would fire the probe forward at a slight downward angle.

The probe's x,y position starts at 0,0. Then, it will follow some trajectory by moving in steps. On each step,
these changes occur in the following order:

The probe's x position increases by its x velocity.
The probe's y position increases by its y velocity.
Due to drag, the probe's x velocity changes by 1 toward the value 0; that is, it decreases by 1 if it is greater than 0,
increases by 1 if it is less than 0, or does not change if it is already 0.
Due to gravity, the probe's y velocity decreases by 1.

Find the initial velocity that causes the probe to reach the highest y position and still eventually be within the target area after any step.

What is the highest y position it reaches on this trajectory?
"""
import logging as log
log.basicConfig(level=log.DEBUG,format="%(asctime)s %(message)s")

def in_targe(x,y,coords):
    return coords[0][0] <= x and x <= coords[0][1] and coords[1][0] <= y and y <= coords[1][1]

def in_bounds(x,y,coords):
    return
def read_vals():
    with open('../data/day17data.txt','r') as file:
        lines = file.read().splitlines()
        coord = lines[0].split(',')
        x = tuple([int(i) for i in coord[0][2:].split('..')])
        y = tuple([int(i) for i in coord[1][3:].split('..')])
        return tuple(x,y)

def part1(coords):
    max_y = -99999999
    for x  in range(0,coords[0][1]):
        for y in range()


if __name__=='__main__':
    coords = read_vals()
    log.info(f"Part 1: {part1(coords)}")