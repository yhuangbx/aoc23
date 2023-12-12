import sys
D = open(sys.argv[1]).read().strip()
lines = D.split('\n')

m = [[col for col in line] for line in lines]

R = len(m[0])
C = len(m)

# print(m)


            
for r in range(R):
    for c in range(C):
        if m[r][c] == 'S':
            sr = r
            sc = c
            print(sr,sc)
            up_valid = (m[r-1][c] in ['|','7','F'])
            right_valid = (m[r][c+1] in ['-','7','J'])
            down_valid = (m[r+1][c] in ['|','J','L'])
            left_valid = (m[r][c-1] in ['-','L','F'])
            assert sum([up_valid, right_valid, down_valid, left_valid]) == 2

            if up_valid and down_valid:
                m[r][c] = '|'
                sd = 0
            elif up_valid and right_valid:
                m[r][c] = 'L'
                sd = 0
            elif up_valid and left_valid:
                m[r][c] = 'J'
                sd = 0
            elif down_valid and right_valid:
                m[r][c] = 'F'
                sd = 2
            elif down_valid and left_valid:
                m[r][c] = '7'
                sd = 2
            elif right_valid and left_valid:
                m[r][c] = '-'
                sd = 1
            else:
                assert False

# print(s_i,s_j)

# up right down left
DR = [-1,0,1,0]
DC = [0,1,0,-1]

r = sr
c = sc
d = sd # start direction
dist = 0

while True:
    dist += 1
    r += DR[d]
    c += DC[d]
    if m[r][c] == '7':
        if d == 0:
            d = 3 
        elif d == 1:
            d = 2
        else:
            print('7',r,c)
            break
    if m[r][c] == 'F':
        if d == 0:
            d = 1
        elif d == 3:
            d = 2
        else:
            print('F',r,c)
            break
    if m[r][c] == 'L':
        if d == 2:
            d = 1
        elif d == 3:
            d = 0
        else:
            print('L',r, c)
            break
    if m[r][c] == 'J':
        if d == 2:
            d = 3
        elif d == 1:
            d = 0
        else: 
            print('J', r, c)
            break
    if (r, c) == (sr, sc):
        print(dist // 2)
        break

