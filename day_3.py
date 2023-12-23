from inputs import day_3
from pprint import pprint

def isadjacent(matrix, cur_row, cur_col):
    coors = [
        [-1,-1], [-1,0], [-1,1], 
        [0,-1], [0,0], [0,1], 
        [1,-1], [1,0], [1,1], 
    ]

    for row, col in coors:
        try:
            char = matrix[cur_row + row][cur_col + col]
            if char not in "0123456789.":
                return True
        except:
            continue
    return False 

def part_1():
    matrix = []
    numbers = []

    for line in day_3.split("\n"):
        if not line:
            continue
        matrix.append([ char for char in line ])

    number = ""
    is_adjacent = False
    for row_idx, row in enumerate(matrix):
        # Thank God I looked for hints because I wasn't taking into account number at the end of the row.
        if number and is_adjacent:
            numbers.append(int(number))
        number = ""
        is_adjacent = False
        for col_idx, col in enumerate(row):
            if col in "0123456789":
                number += col
                if not is_adjacent:
                    is_adjacent = isadjacent(matrix, row_idx, col_idx)
            elif number:
                # print(number, is_adjacent)
                if is_adjacent:
                    numbers.append(int(number))
                number = ""
                is_adjacent = False


    # print(numbers)
    pprint(sum(numbers))

# part_1()
    
def get_number(line, cur_index):
    """ Get the number in a string at any given index. """

    start = 0
    while (cur_index - start) > 0 and line[cur_index - (start + 1)].isdigit():
        start += 1

    end = 0
    len_line = len(line)
    while (cur_index + end) < len_line and line[cur_index + end].isdigit():
        end += 1

    # print("--", line[cur_index - start : cur_index + end], "--")
    return int(line[cur_index - start : cur_index + end])

    
def get_pair(matrix, cur_row, cur_col):
    pair = []
    coors = [
        [-1,-1], [-1,0], [-1,1], 
        [0,-1], [0,0], [0,1], 
        [1,-1], [1,0], [1,1], 
    ]

    for row, col in coors:
        try:
            char: str = matrix[cur_row + row][cur_col + col]

            if char.isdigit():
                number = get_number(matrix[cur_row + row], cur_col + col)
                if number not in pair:
                    pair.append(number)
        except:
            continue

    if len(pair) == 2:
        return pair 

    return False

def part_2():
    total = 0
    matrix = []

    for line in day_3.split("\n"):
        if not line:
            continue
        # matrix.append([ char for char in line ])
        matrix.append(line)

    for row_idx, row in enumerate(matrix):
        pair = []
        for col_idx, col in enumerate(row):
            if col == "*":
                pair = get_pair(matrix, row_idx, col_idx)
                if pair:
                    total += pair[0] * pair[1]

    print(total)

part_2()