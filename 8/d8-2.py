import sys
import math
D = open(sys.argv[1]).read().strip()
lines = D.split('\n')

directions = lines[0]
GO = {}
for line in lines[2:]:
    key, LR = line.split(' = ')
    left, right = LR[1:-1].split(', ')
    GO[key] = [left, right]

# print(GO)

start_positions=[]
for key in GO.keys():
    if key.endswith('A'):
        start_positions.append(key)

print(start_positions)

def find_directions(directions, GO, step):
    for char in directions:
        if char == 'L':
            step = GO[step][0]
        else:
            step = GO[step][1]       
    return step.endswith('Z')

m = 1
lcm_list = []

for pos in start_positions:
    mdirections = directions * m
    flag = False
    while not flag:
        m += 1
        mdirections = directions * m
        flag = find_directions(mdirections, GO, pos)
        print(pos,m)
    lcm_list.append(m)
    m = 1
    

print(lcm_list)
# [59, 79, 61, 43, 67, 53]


ans = 1
for x in lcm_list:
    ans = (x * ans) //math.gcd(x,ans)

print(ans)
print(ans * len(directions))