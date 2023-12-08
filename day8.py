import fileinput
import math

lines = [line.strip() for line in fileinput.input()]

instructions = lines[0]

left_moves = {}
right_moves = {}

for line in lines[2:]:
    src = line[0:3]
    left = line[7:10]
    right = line[12:15]

    left_moves[src] = left
    right_moves[src] = right

N = len(instructions)

def find_len(start = 'AAA', end = lambda x : x == 'ZZZ'):
    i = 0
    curr = start
    while not end(curr):
        c = instructions[i % N]
        if c == 'L':
            curr = left_moves[curr]
        else:
            curr = right_moves[curr]

        i += 1

    return i

# Part 1
print(find_len())

# Part 2
print(math.lcm(*(find_len(start=state, end=lambda x : x[2] == 'Z') for state in (state for state in left_moves.keys() if state[2] == 'A'))))


