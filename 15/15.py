import sys
from collections import defaultdict
D = open(sys.argv[1]).read().strip()
# G = [[c for c in r] for r in D.split('\n')]

def convert(s, v):
    for c in s:
        v += ord(c)
        v *= 17
        v = v %256
    return v



l = D.split(',')

# ans = 0
# for s in l:
#     v = 0
#     for c in s:
#         v = convert(c,v)
#     print(v)
#     ans += v
# print(ans)


boxes = {i: defaultdict(dict) for i in range(256)}
for s in l:
    if '=' in s:
        label , fp = s.split('=')
        bn = convert(label,0)
        boxes[bn][label] = int(fp)
    elif '-' in s:
        label=s.split('-')[0]
        bn = convert(label,0)
        if label in boxes[bn].keys():
            del boxes[bn][label]

ans = 0
for bn in boxes.keys():
    
    bv = 0
    if len(boxes[bn]) > 0:
        i = 1
        for k in boxes[bn].keys():
            bv += (bn+1)*i*boxes[bn][k]
            i += 1
            # print(bn, k, boxes[bn][k],bv)
        ans += bv

print(ans)

