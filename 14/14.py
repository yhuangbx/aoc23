import sys
from collections import defaultdict
D = open(sys.argv[1]).read().strip()
G = [[c for c in r] for r in D.split('\n')]

def print_G(G):
    for row in G:
        print(row)

# print_G(G)

O = defaultdict(list)
H = defaultdict(list)
# wt = list(range(1,len(G)+1))[::-1]


for i in range(len(G)):
    for j in range(len(G[0])):
        if G[i][j] == 'O':
            O[j].append(i)
        elif G[i][j] == '#':
            H[j].append(i)

# print(O)
# print(H)
ans = 0
for c in range(len(G[0])):
    min_o = 0
    for o in O[c]:
        
        for h in H[c]:
            if o > h:
                min_o = max(min_o,h+1)
            
        ans += len(G) - min_o
        # print(o,c, 10 - min_o)
        min_o += 1
        

print(ans)