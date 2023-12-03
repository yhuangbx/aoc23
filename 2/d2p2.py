#!/usr/bin/python3

import re

file_path = "input.txt"

power = 0

with open(file_path, 'r') as file:
    for line in file:
        match_game = re.search(r'Game (\d+):', line)
        if match_game:
            game_num = int(match_game.group(1))
        # find all the reds
        match_red = re.findall(r'(\d+) red', line)
        match_blue = re.findall(r'(\d+) blue', line)
        match_green = re.findall(r'(\d+) green', line)
        max_blue, max_green, max_red = 0, 0, 0

        if len(match_red) > 0:
            match_red = list(map(int, match_red))
            max_red = max(match_red)
        if len(match_blue) > 0:
            match_blue = list(map(int, match_blue))
            max_blue = max(match_blue)
        if len(match_green) > 0:
            match_green = list(map(int, match_green))
            max_green = max(match_green)
        
        power += max_red * max_green * max_blue
        print(game_num, power, max_blue, max_green, max_red)

print(power)
