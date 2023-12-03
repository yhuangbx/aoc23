#!/usr/bin/python3
# Determine which games would have been possible if the bag had been loaded with only 
# 12 red cubes, 13 green cubes, and 14 blue cubes. 
# What is the sum of the IDs of those games?

import re

file_path = "input.txt"

game_num_sum = 0

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
        
        if max_red <= 12 and max_green <= 13 and max_blue <= 14:
            print(game_num, max_blue, max_green, max_red)
            game_num_sum += game_num

print(game_num_sum)