#!/usr/bin/python3
import re


file_path = 'input.txt'
with open(file_path, 'r') as file:
    total = 0
    for line in file:
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
        if count > 0:
            total += 2 ** (count - 1)
file.close()

print(total)