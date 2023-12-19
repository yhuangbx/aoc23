import sys
from collections import defaultdict, deque

sys.setrecursionlimit(10000000)

def print_matrix(G):
    for row in G:
        print(' '.join(row))

def flood_fill(matrix, x, y, target, replacement):
    """
    Perform flood-fill on the matrix starting from position (x, y).
    Replace all occurrences of the target value with the replacement value.
    """
    if matrix[x][y] != target:
        return

    matrix[x][y] = replacement

    directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]

    for dx, dy in directions:
        new_x, new_y = x + dx, y + dy
        if 0 <= new_x < len(matrix) and 0 <= new_y < len(matrix[0]):
            flood_fill(matrix, new_x, new_y, target, replacement)

D = open(sys.argv[1]).read().strip()
L = D.split('\n')
# G = [[c for c in r] for r in D.split('\n')]

# R = len(G)
# C = len(G[0])
directions = {'U':(-1,0),'D':(1,0),'L':(0,-1),'R':(0,1)}

r = 0
c = 0
SEEN = set()
SEEN.add((r,c))
travels = []

for row in L:
    direction, steps, color = row.split()
    travels.append((direction,steps,color))
    dr, dc = directions[direction]
    for _ in range(int(steps)):
        r += dr
        c += dc
        SEEN.add((r,c))

min_r = min(r for r,_ in SEEN)
max_r = max(r for r,_ in SEEN)
min_c = min(c for _,c in SEEN)
max_c = max(c for _,c in SEEN)

print(min_r, max_r, min_c, max_c)

G = [['.' for _ in range(min_c,max_c + 1)] for _ in range(min_r, max_r + 1)]

for x, y in SEEN:
    # print(x,y)
    # print_matrix(G)
    G[x - min_r][y-min_c] = '#'


start_r = (max_r - min_r) // 2
start_c = (max_c - min_c) // 2
print(start_r)
print(start_c)
# flood_fill(G,start_r,start_c, '.', '#')
# print_matrix(G)

directions = [(1,0),(0,1),(-1,0),(0,-1)]
queue = deque([(start_r,start_c)])

while queue:
    r, c = queue.popleft()

    if G[r][c] == '.':
        G[r][c] = '#'

        for dr, dc in directions:
            new_r, new_c = r + dr, c+dc
            if 0 <= new_r <len(G) and 0<= new_c < len(G[0]):
                queue.append((new_r,new_c))

print_matrix(G)

ans =0
for row in G:
    ans += row.count('#')

print(ans)


