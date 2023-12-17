import sys
from collections import defaultdict

sys.setrecursionlimit(5000)

D = open(sys.argv[1]).read().strip()
G = [[c for c in r] for r in D.split('\n')]

L = len(G)
W = len(G[0])

E = {}

# UP: travel('U',r-1,c,G)
# DOWN: travel('D',r+1,c,G)
# LEFT: travel('L',r,c-1,G)
# RIGHT: travel('R',r,c+1,G)

def travel(dir,r,c,G):
    if 0 <= r < L and 0 <= c < W: 
        if (r,c) not in E:
            E[(r,c)] = dir
        elif E[(r,c)] == dir:
            print("loop detected, terminate")
            return
        if dir == 'R':
            if G[r][c] == '|':
                print(f"Going Up from ({r}, {c})")
                travel('U',r-1,c,G)
                print(f"Going Down from ({r}, {c})")
                travel('D',r+1,c,G)
            elif G[r][c] == '\\':
                print(f"Going Down from ({r}, {c})")
                travel('D',r+1,c,G)
            elif G[r][c] == '/':
                print(f"Going Up from ({r}, {c})")
                travel('U',r-1,c,G)
            else:
                print(f"Going Right from ({r}, {c})")
                travel('R',r,c+1,G)
        elif dir == 'U':
            if G[r][c] == '-':
                print(f"Going Left from ({r}, {c})")
                travel('L',r,c-1,G)
                print(f"Going Right from ({r}, {c})")
                travel('R',r,c+1,G)
            elif G[r][c] == '\\':
                print(f"Going Left from ({r}, {c})")
                travel('L',r,c-1,G)
            elif G[r][c] == '/':
                print(f"Going Right from ({r}, {c})")
                travel('R',r,c+1,G)
            else:
                print(f"Going Up from ({r}, {c})")
                travel('U',r-1,c,G)
        elif dir == 'L':
            if G[r][c] == '|':
                print(f"Going Up from ({r}, {c})")
                travel('U',r-1,c,G)
                print(f"Going Down from ({r}, {c})")
                travel('D',r+1,c,G)
            elif G[r][c] == '\\':
                print(f"Going Up from ({r}, {c})")
                travel('U',r-1,c,G)
            elif G[r][c] == '/':
                print(f"Going Down from ({r}, {c})")
                travel('D',r+1,c,G)
            else:
                print(f"Going Left from ({r}, {c})")
                travel('L',r,c-1,G)
        elif dir == 'D':
            if G[r][c] == '-':
                print(f"Going Left from ({r}, {c})")
                travel('L',r,c-1,G)
                print(f"Going Right from ({r}, {c})")
                travel('R',r,c+1,G)
            elif G[r][c] == '\\':
                print(f"Going Right from ({r}, {c})")
                travel('R',r,c+1,G)
            elif G[r][c] == '/':
                print(f"Going Left from ({r}, {c})")
                travel('L',r,c-1,G)
            else:
                print(f"Going Down from ({r}, {c})")
                travel('D',r+1,c,G)

    else:
        print("Out of bound")
        return

def print_board(E,W,L):
    Board = [[c for c in '.'* W] for r in '.' * L]
    for i in range(L):
        for j in range(W):
            if (i,j) in E:
                Board[i][j] = '#'

    for r in Board:
        print('.'.join(i for i in r))


max_length = 0
# Travel Downward:
for i in range(W):
    E = {}
    travel('D',0,i,G)
    v = len(E)
    if v > max_length:
        max_length = v

# Travel Upward:
for i in range(W):
    E = {}
    travel('U',L-1,i,G)
    v = len(E)
    if v > max_length:
        max_length = v

# Travel Right:
for i in range(L):
    E = {}
    travel('R',i,0,G)
    v = len(E)
    if v > max_length:
        max_length = v

# Travel Left:
for i in range(L):
    E = {}
    travel('R',i,W-1,G)
    v = len(E)
    if v > max_length:
        max_length = v

print(max_length)

# print(E)
# print(len(E))
# print_board(E,W,L)

