import fileinput

grid = [line.strip() for line in fileinput.input()]

n = len(grid)
m = len(grid[0])


DIRECTIONS = "NESW"

def move(row, col, direction):
    if direction == 'E':
        return row, col + 1, direction
    elif direction == 'W':
        return row, col - 1, direction
    elif direction == 'N':
        return row - 1, col, direction
    elif direction == 'S':
        return row + 1, col, direction

def turn_left(direction):
    return DIRECTIONS[(DIRECTIONS.index(direction) - 1) % 4]

def turn_right(direction):
    return DIRECTIONS[(DIRECTIONS.index(direction) + 1) % 4]

def simulate(col = 0, row = 0, direction = 'E'):
    energized = set()
    seen = set()
    beams = [(row, col, direction)]

    while beams:
        row, col, direction = beams.pop()

        if not (row >= 0 and row < n and col >= 0 and col < m) or (row, col, direction) in seen:
            continue

        c = grid[row][col]

        seen.add((row, col, direction))
        energized.add((row, col))

        # Do nothing
        if c == '.' or (c == '-' and direction in 'EW') or (c == '|' and direction in 'NS'):
            beams.append(move(row, col, direction))

        # Split the beam
        elif c in '-|':
            left = turn_left(direction)
            right = turn_right(direction)

            beams.append(move(row, col, left))
            beams.append(move(row, col, right))
        
        elif c == '/':
            if direction in 'EW':
                beams.append(move(row, col, turn_left(direction)))
            else:
                beams.append(move(row, col, turn_right(direction)))

        else:
            if direction in 'EW':
                beams.append(move(row, col, turn_right(direction)))
            else:
                beams.append(move(row, col, turn_left(direction)))

    return len(energized)

# Part 1
print(simulate())

# Part 2
def get_options():
    for row in range(n):
        yield 0, row, 'E'
        yield m -1, row, 'W'
    
    for col in range(m):
        yield col, 0, 'S'
        yield col, n-1, 'N'

print(max(map(lambda option: simulate(*option), get_options())))