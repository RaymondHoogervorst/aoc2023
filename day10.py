import fileinput

DIRECTIONS = {
    '-' : 'EW',
    '|' : 'NS',
    'L' : 'NE',
    'F' : 'SE',
    '7' : 'SW',
    'J' : 'NW',
}

OPPOSITE = {
    'E' : 'W',
    'W' : 'E',
    'N' : 'S',
    'S' : 'N',
}

lines = list(map(list, map(str.strip, fileinput.input())))


# find S coords
for y, line in enumerate(lines):
    for x, c in enumerate(line):
        if c == 'S':
            sx, sy = x, y
            break

def step(y, x, dir):
    if dir == 'E': x += 1
    elif dir == 'W': x -= 1
    elif dir == 'N': y -= 1
    elif dir == 'S': y += 1
    return y, x

def replace(y, x, c):
    lines[y][x] = c

def traverse(y, x, dir):

    route = [(y, x)]

    first_dir = dir

    while (c := lines[y][x]) != 'S':

        opp = OPPOSITE[dir]

        c = lines[y][x]
        if c == '.' : return False

        sides = DIRECTIONS[c]
        if opp not in sides: return False

        dir = sides[0] if sides[0] != opp else sides[1]
        y, x = step(y, x, dir)

        route.append((y, x))

    opp = OPPOSITE[dir]

    # Find c with both first_dir and opp
    for key, value in DIRECTIONS.items():
        if first_dir in value and opp in value:
            replace(y, x, key)
            break

    length = len(route)
    route = set(route)
    for x in range(len(lines[0])):
        for y in range(len(lines)):
            if (y, x) not in route:
                replace(y, x, '.')

    return length

for dir in 'ESWN':
    y, x = step(sy, sx, dir)
    length = traverse(y, x, dir)
    if length is not False:
        break


# Part 1 - Distance to furthest point of loop
print(length // 2)

# Part 2 - Area enclosed by loop

area = 0
for line in lines:
    # True if either in loop or along top edge
    # False if either out of loop or along bottom edge
    state = False

    for c in line:
        if c == '.' and state:
            area += 1
        
        elif c == '|' or c == '7' or c == 'F':
            state = not state

        x += 1
    y += 1
print(area)