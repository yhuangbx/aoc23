import sys
from collections import defaultdict


D = open(sys.argv[1]).read().strip()
lines = D.split('\n')

times = list(map(int,lines[0].split(':')[1].split()))
distances = list(map(int, lines[1].split(':')[1].split()))

result = []

for i, time in enumerate(times):
    count = 0
    for v in range(time + 1):
        # speed = v
        if v * (time - v) > distances[i]:
            count += 1
    result.append(count)


p1 = 1
for item in result:
    p1 *= item

print(p1)

time2 = int(lines[0].split(':')[1].replace(' ',''))
distance2 = int(lines[1].split(':')[1].replace(' ',''))

print(time2, distance2)

count = 0
for v in range(time2+1):
    if v * (time2 - v) > distance2:
        count += 1
print(count)
    