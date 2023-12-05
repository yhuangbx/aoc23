#!/usr/bin/python3
import re
file_path = "input.txt"


def read_file_to_matrix(file_path):
    with open(file_path, 'r') as file:
        lines = file.readlines()

        matrix = [list(line.strip()) for line in lines]

        return matrix

def check_part_num(matrix,i,j):
    part_num = ''

    left_boundary = j - 1

    while j < len(matrix[0]) and matrix[i][j].isdigit():
        part_num += matrix[i][j]
        j += 1
    
    right_boundary = min(len(matrix[0])-1, j)

    upper_boundary = max(0, i - 1)
    lower_boundary = min(len(matrix)-1, i + 1)
    
    return int(part_num), left_boundary, right_boundary, upper_boundary, lower_boundary
    
def check_valid_part(left_boundary, right_boundary, upper_boundary, lower_boundary, matrix):
    for i in range(upper_boundary, lower_boundary+1):
        for j in range(left_boundary, right_boundary + 1):
            if matrix[i][j] != '.' and not matrix[i][j].isalnum():
                return True
    return False

def calc_part_num(matrix):
    l = len(matrix)
    w = len(matrix[0])
    i = 0
    total = 0
    while i < l :
        j = 0
        while j < w :
            if matrix[i][j].isdigit():
                # print(i,j,matrix[i][j])
                part_num, left_boundary, right_boundary, upper_boundary, lower_boundary = check_part_num(matrix, i, j)
                if check_valid_part(left_boundary, right_boundary, upper_boundary, lower_boundary, matrix):
                    # print(left_boundary, right_boundary, upper_boundary, lower_boundary,part_num)
                    total += part_num
                j = right_boundary
                
            else:
                j += 1
        i += 1

    return total
            


if __name__ == '__main__':
    matrix = read_file_to_matrix('input.txt')
    print(calc_part_num(matrix))