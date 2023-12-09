import sys
D = open(sys.argv[1]).read().strip()
lines = D.split('\n')

directions = lines[0]
GO = {}
for line in lines[2:]:
    key, LR = line.split(' = ')
    left, right = LR[1:-1].split(', ')
    GO[key] = [left, right]

step = 'AAA'
m = 0
while step != 'ZZZ':
    for char in directions:
        if char == 'L':
            step = GO[step][0]
        else:
            step = GO[step][1]
        m += 1
        print(m, char, step)
print(m)