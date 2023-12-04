import fileinput
from collections import defaultdict

board = [line.strip() for line in fileinput.input()]

n = len(board[0])
m = len(board)

gear_numbers = defaultdict(list)

def get_gears(y, x):
    gear_list = []
    if board[y][x] == '*': gear_list.append((y, x))
    if y > 0 and board[y - 1][x] == '*': gear_list.append((y - 1, x))
    if y < m - 1 and board[y + 1][x] == '*': gear_list.append((y + 1, x))
    return gear_list

s = 0
for y, line in enumerate(board):
    touches_symbol = False
    curr_num = 0
    local_gears = []

    for x, c in enumerate(line):
        col_gears = get_gears(y, x)
        local_gears += col_gears

        if c.isdigit():
            curr_num = curr_num * 10 + int(c)
        else:
            if curr_num:
                for gear in local_gears: gear_numbers[gear].append(curr_num)

            local_gears = col_gears
            curr_num = 0

    if curr_num:
        for gear in local_gears: gear_numbers[gear].append(curr_num)

print(sum(numbers[0] * numbers[1] for numbers in gear_numbers.values() if len(numbers) == 2))