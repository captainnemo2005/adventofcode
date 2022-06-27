"""
Inputs:

NNCB

CH -> B
HH -> N
CB -> H
NH -> C
HB -> C
HC -> B
HN -> C
NN -> C
BH -> H
NC -> B
NB -> B
BN -> B
BB -> N
BC -> B
CC -> N
CN -> C

Outputs:

Template:     NNCB
After step 1: NCNBCHB
After step 2: NBCCNBBBCBHCB
After step 3: NBBBCNCCNBBNBNBBCHBHHBCHB
After step 4: NBBNBNBBCCNBCNCCNBBNBBNBBBNBBNBBCBHCBHHNHCBBCBHCB
"""
import logging as log
log.basicConfig(level=log.DEBUG, format="%(asctime)s %(message)s")
def read_vals()->list:
    with open('../data/day14data.txt','r') as file:
        lines = file.read().splitlines()
        x = [line for line in lines]
        template = x[0]
        polymers = {}
        for i in range(2,len(x)):
            polymers[x[i].split('->')[0][:2]] = x[i].split('->')[0][:1]+x[i].split(' ')[2] + x[i].split('->')[0][1:2]
        return template, polymers
def part1(template, polymers,step) -> int:
    for i in range(1,step):
        newtemplate = ""
        for j in range(len(template)):
            if j+1 < len(template):
                if j == 0:
                    newtemplate += polymers[template[j:j+2]]
                else:
                    newtemplate += polymers[template[j:j+2]][1:]
        template = newtemplate
        log.info(f"Finish step {i}")
    cnt = {}
    for ch in list(set(template)):
        cnt[ch] = template.count(ch)
    cnt = dict(sorted(cnt.items(), key=lambda item: item[1]))
    return list(cnt.items())[-1][1] - list(cnt.items())[0][1]

def part2(step):
    with open('../data/day14data.txt') as f:
        lines = f.read().splitlines()
    poly = lines[0]
    mp = {}
    cnt = {}
    for line in lines[2:]:
        cur = line.split(' -> ')
        mp[cur[0]] = cur[1]

    for i in range(len(poly) - 1):
        cnt[poly[i:i+2]] = cnt.get(poly[i:i+2],0) +1
    log.info(cnt)
    log.info(mp)
    for i in range(step):
        cnt2 = {}
        for pair in cnt:
            cnt2[pair[0] + mp[pair]] = cnt2.get(pair[0] + mp[pair],0) + cnt[pair]
            log.info(cnt2)
            cnt2[mp[pair] + pair[1]] = cnt2.get(mp[pair] + pair[1],0) + cnt[pair]
            log.info(cnt2)
        cnt = cnt2
    lst = {}
    for pair in cnt:
        lst[pair[0]] = lst.get(pair[0],0) + cnt[pair]
    lst[poly[-1]] += 1
    return max(lst.values()) - min(lst.values())
if __name__ == '__main__':
    template, polymers = read_vals()
    # log.info(f'Part 1: {part1(template, polymers,10)}')
    log.info(f'Part 2: {part2(40)}')