import sys

D = open(sys.argv[1]).read().strip()
lines = D.split('\n')

p1 = 0
for line in lines:
    print(line)
    winning, cards = line.split(':')[1].split('|')
    winning_num = [int(x) for x in winning.strip().split(' ')]
    # print(winning_num)
    cards_num = [int(x) for x in cards.strip().split(' ') if x != '']
    # print(cards_num)
    matches = len(set(winning_num) & set(cards_num))
    print(matches)
    if matches > 0:
        p1 += 2 ** (matches - 1)

print(p1)