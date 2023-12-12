import sys
D = open(sys.argv[1]).read().strip()
lines = D.split('\n')

def x(l):
    if all(e == l[0] for e in l):
        return l[0]
    else:
        return l[-1] + x([ai - bi for ai, bi in zip(l[1:], l[:-1])])

def p2(l):
    if all(e == l[0] for e in l):
        return l[0]
    else:
        return l[0] - p2([ai - bi for ai, bi in zip(l[1:], l[:-1])])

# print(p2([10 ,13 ,16 ,21 ,30 ,45]))
# print(p2([0, 3, 6, 9, 12, 15]))

ans = 0
ans2 = 0

for line in lines:
    line = list(map(int,line.split()))
    # print(line)
    ans += x(line)
    ans2 += p2(line)



print(ans)
print(ans2)