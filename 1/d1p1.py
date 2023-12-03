#!/usr/bin/python3

file_path = "trebuchet.txt"

val = 0

with open(file_path, 'r') as file:
    for line in file:
        digits = []
        for char in line:
            if char.isdigit():
                digits.append(char)
        to_add_num = int(digits[0])*10 + int(digits[-1])
        val += to_add_num


print(val)