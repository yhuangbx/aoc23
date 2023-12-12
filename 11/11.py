import sys
D = open(sys.argv[1]).read().strip()
lines = D.split('\n')

m = [[col for col in line] for line in lines]

# expand
r_e = []
c_e = []

col_indexes = [i for i in range(len(m[0]))]
rol_indexes = [i for i in range(len(m))]

for i,row in enumerate(m):
    if all(x == '.' for x in row):
        r_e.append(i)


for col_index in col_indexes:
    if all(row[col_index] == '.' for row in m):
        c_e.append(col_index)

cr = []
cc = []
for i in range(len(m)):
    for j in range(len(m[0])):
        if m[i][j] == '#':
            cr.append(i)
            cc.append(j)

# print(list(zip(cr,cc)))


# pair = 1
parts = [1,10**6-1]

for part in parts:
    ans = 0
    for i in range(len(cc)):
        for j in range(i, len(cc)):
            dist = abs(cr[j]-cr[i]) + abs(cc[j] - cc[i]) 
            for er in r_e:
                if min(cr[j],cr[i]) <= er <= max(cr[j],cr[i]):
                    dist += part
            for ec in c_e:
                if min(cc[i],cc[j]) <= ec <= max(cc[i],cc[j]):
                    dist += part
            ans += dist

            # print(pair, dist, (cr[i],cc[i]),(cr[j],cc[j]))
            # pair+=1
            j += 1

    print(ans)