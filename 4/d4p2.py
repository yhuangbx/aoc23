#!/usr/bin/python3
import re
from collections import defaultdict

file_path = 'input.txt'

def check_winnings(line):
    winnings = line.split(':')[1].split('|')[0].strip()
    winnings = re.split(r'\s+', winnings)
    winnings = list(map(int,winnings))
    matchings = line.split(':')[1].split('|')[1].strip()
    matchings = re.split(r'\s+', matchings)
    matchings = list(map(int,matchings))
    count = 0
    for number in matchings:
        if number in winnings:
            count += 1
    return count

# How do I do this recursively?
# def spawn_instances(i, lines, count):
#     if count == 0:
#         return 0
    
#     num_of_matches = check_winnings(line[i])
#     total_copies += spawn_instances(i+1, lines, num_of_matches)


with open(file_path, 'r') as file:
    lines = [line.rstrip() for line in file.readlines()]
file.close()

copies = defaultdict(int)


for i, line in enumerate(lines):
    copies[i] += 1
    num_of_matches = check_winnings(line)
    for j in range(num_of_matches):
        copies[i+j+1] += copies[i]

print(sum(copies.values()))