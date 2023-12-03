#!/usr/bin/python3
import re
file_path = "trebuchet.txt"

val = 0

map = {
    'one': 'o1e',
    'two': 't2o',
    'three': 't3e',
    'four': 'f4r',
    'five': 'f5e',
    'six': 's6x',
    'seven': 's7n',
    'eight': 'e8t',
    'nine': 'n9e'
}


with open(file_path, 'r') as file:
    for line in file:
        for key in map.keys():
            line = re.sub(key, f"{(map[key])}", line)
        digits = []
        for char in line:
            if char.isdigit():
                digits.append(char)
        to_add_num = int(digits[0])*10 + int(digits[-1])
        val += to_add_num


print(val)