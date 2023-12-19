import sys
from collections import defaultdict

def print_matrix(G):
    for row in G:
        print(' '.join(row))


D = open(sys.argv[1]).read().strip()
L = D.split('\n')


r = 0
c = 0
SEEN = set()
SEEN.add((r,c))

directions = [(0,1),(1,0),(0,-1),(-1,0)]

for row in L:
    steps = int(row.split()[-1][2:-2],16)
    direction = int(row.split()[-1][-2:-1])
    dr, dc = directions[direction]
    for _ in range(steps):
        r+=dr
        c+=dc
        SEEN.add((r,c))

min_r = min(r for r,_ in SEEN)
max_r = max(r for r,_ in SEEN)
min_c = min(c for _,c in SEEN)
max_c = max(c for _,c in SEEN)

G = [['.' for _ in range(min_c,max_c + 1)] for _ in range(min_r, max_r + 1)]
for r ,c in SEEN:
    G[r-min_r][c-min_c] = '#'

print_matrix(G)