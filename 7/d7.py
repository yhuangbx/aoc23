import sys
from collections import defaultdict, Counter


D = open(sys.argv[1]).read().strip()
lines = D.split('\n')

card_map = {
    "A":13, 
    "K":12, 
    "Q":11, 
    "J":10, 
    "T":9, 
    "9":8, 
    "8": 7, 
    "7": 6, 
    "6": 5, 
    "5": 4, 
    "4": 3, 
    "3": 2,
    "2": 1
}

def strength(hand):
    hand = hand.replace('T', chr(ord('9')+1))
    hand = hand.replace('J', chr(ord('9')+2))
    hand = hand.replace('Q', chr(ord('9')+3))
    hand = hand.replace('K', chr(ord('9')+4))
    hand = hand.replace('A', chr(ord('9')+5))
    C = Counter(hand)
    if list(C.values()) == [5]:
        return(10,hand)
    elif sorted(C.values()) == [1,4]:
        return(9, hand)
    elif sorted(C.values()) == [2,3]:
        return(8, hand)
    elif sorted(C.values()) == [1,1,3]:
        return(7, hand)
    elif sorted(C.values()) == [1,2,2]:
        return(6, hand)
    elif sorted(C.values()) == [1,1,1,2]:
        return(5, hand)
    else:
        return(4, hand)


hands = []
score = 0
for line in lines:
    hand, bid = line.split()
    hands.append((hand,bid))
    # print(card)
    # print(score)

hands = sorted(hands, key=lambda hb:strength(hb[0]))

print(hands)
for i, (h,b) in enumerate(hands):
    score += (i+1) * int(b)
print(score)