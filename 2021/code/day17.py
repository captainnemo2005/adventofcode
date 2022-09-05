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

ss = 500
def in_bounds(x,y):
    return -ss <= x and x <= ss and -ss <= y and y <= 10000

def in_target(x, y, target_x, target_y):
	return target_x[0] <= x and x <= target_x[1] and target_y[0] <= y and y <= target_y[1]

def read_vals():
    with open('../data/day17data.txt','r') as file:
        lines = [s[2:].split("..") for s in file.read().strip().replace("target area: ", "").split(", ")]
    return [(int(lines[0][0]), int(lines[0][1])), (int(lines[1][0]), int(lines[1][1]))]


def brute_force(vals) -> list:
    r_x = range(vals[0][0],vals[0][1]+1)
    r_y = range(vals[1][0],vals[1][1]+1)

    tmp = [fire_probe(x,y,r_x,r_y) for x in range(vals[0][1] +1) for y in range(-1000,1000)]
    return [velocity for velocity in tmp if velocity[2] is not None]

def fire_probe(vel_x,vel_y,goal_x,goal_y):
     vx,vy = vel_x, vel_y
     x,y = 0,0
     max_y = -999999999
     while x+vx < goal_x.stop:
         x += vx
         y += vy
         max_y = max(y,max_y)
         vx += 0 if vx == 0 else -1 if vx > 0 else 1
         vy -= 1
         if vx == 0 and (x < goal_x.start or y < goal_y.start):
             break
         if x in goal_x and y in goal_y:
             return vel_x, vel_y, max_y
     return vel_x, vel_y, None

def part1(vals):
    return max(vals, key = lambda x:x[2])[2]

def part2(vals):
    return len(vals)

if __name__=='__main__':
    vals = read_vals()
    vals = brute_force(vals)
    log.info(f"Part 1: {part1(vals)}")
    log.info(f"Part 2: {part2(vals)}")
