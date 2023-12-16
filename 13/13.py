import sys
D = open(sys.argv[1]).read().strip()


patterns = D.split('\n\n')
ans = 0

part2 = False

for pattern in patterns:
    P = [[c for c in r] for r in pattern.split('\n')]
    R = len(P)
    C = len(P[0])
    # vertical symmetery
    for i in range(C-1):
        badness = 0
        for j in range(C):
            left = i - j
            right = i + j + 1
            if 0 <= left < right < C:
                for r in range(R):
                    if P[r][left] != P[r][right]:
                        badness += 1
        if badness == (1 if part2 else 0):
            print(i+1)
            ans += i + 1
    
    # horizontal symmetry
    for i in range(R-1):
        badness = 0
        for j in range(R):
            up = i - j
            down = i + j + 1
            if 0 <= up < down < R:
                for c in range(C):
                    if P[up][c] != P[down][c]:
                        badness += 1
        if badness == (1 if part2 else 0): 
            print((i+1)*100)
            ans += (i+1)*100

print(ans)

