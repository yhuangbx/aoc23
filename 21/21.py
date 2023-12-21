import sys
from collections import defaultdict, deque

# sys.setrecursionlimit(10000000)

D = open(sys.argv[1]).read().strip()
L = D.split('\n')
G = [[c for c in r] for r in D.split('\n')]

R = len(G)
C = len(G[0])

steps = 64
p = set()

def find_possibilities(G, r, c, steps):
    d = [(-1,0),(0,1),(1,0),(0,-1)]
    # score = 0
    if steps == 0:
        print(r,c,steps)
        p.add((r,c))
        return

    for dr, dc in d:
        rr = r + dr
        cc = c + dc
        if 0 <= rr < R and 0 <= cc < C:
            if G[rr][cc] != '#':
                find_possibilities(G, rr, cc, steps-1)
    # return score
            
for r in range(R):
    for c in range(C):
        if G[r][c] == 'S':
            find_possibilities(G,r,c,steps)


print(p,len(p))