"""
start-A
start-b
A-c
A-b
b-d
A-end
b-end

output:
start,A,b,A,c,A,end
start,A,b,A,end
start,A,b,end
start,A,c,A,b,A,end
start,A,c,A,b,end
start,A,c,A,end
start,A,end
start,b,A,c,A,end
start,b,A,end
start,b,end
"""

import logging as log
log.basicConfig(level=log.DEBUG, format="%(asctime)s %(message)s")

def read_data()->list:
    with open('../data/day12data.txt', 'r') as file:
        lines = file.read().splitlines()
        return [line for line in lines]

def part1(lines):
    adj = get_adj(lines)
    cur = 'start'
    path = ['start']
    return recur(cur,path,adj)
def get_adj(lines) -> dict:
    adj = {}
    for line in lines:
        v1, v2 = line.split('-')
        adj.setdefault(v1,[]).append(v2)
        adj.setdefault(v2,[]).append(v1)
    return adj

def recur(cur,path,adj):
    if cur == 'end':
        return 1
    out = 0
    for child in adj[cur]:
        if child.lower() != child or child not in path:
            out += recur(child,path + [child], adj)
    return out

def part2(lines):
    adj = get_adj(lines)

    cur = 'start'
    path = ['start']
    return recur_part2(cur, path, adj, False)

def recur_part2(cur,path,adj,twice):
    if cur == 'end':
        return 1
    out = 0
    for child in adj[cur]:
        if child == 'start':
            continue
        elif child.lower() != child or child not in path:
            out += recur_part2(child, path + [child], adj, twice)
        elif path.count(child) == 1 and not twice:
            out += recur_part2(child, path + [child], adj, True)
    return out
if __name__ == '__main__':
    log.info(f"Part 1: {part1(read_data())}")
    log.info(f"Part 2: {part2(read_data())}")