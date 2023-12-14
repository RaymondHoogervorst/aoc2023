import fileinput

lines = [list(line.strip()) for line in fileinput.input()]

n = len(lines)
m = len(lines[0])

def get_load(lines):
    res = 0
    for row in range(n):
        for col in range(m):
            if lines[row][col] == 'O':
                res += n - row
    return res

def move(lines, horizontal = False, reverse = False):
    main_len, cross_len = (m, n) if horizontal else (n, m)

    direction = -1 if reverse else 1

    for i in range(cross_len):
        k = main_len - 1 if reverse else 0

        for j in (range(cross_len-1, -1, -1) if reverse else range(cross_len)):
            c = lines[i][j] if horizontal else lines[j][i]
            if c == 'O':
                if horizontal:
                    lines[i][j] = '.'
                    lines[i][k] = 'O'
                else:
                    lines[j][i] = '.'
                    lines[k][i] = 'O'
                k += direction
            elif c == '#':
                k = j + direction

def cycle(lines):
    move(lines, False, False)   # North
    move(lines, True, False)    # West
    move(lines, False, True)    # South
    move(lines, True, True)     # East

def hashable(lines):
    return tuple(map(tuple, lines))

def cycle_n_times(lines, n_iters=1_000_000_000):
    history = []
    history_map = {}

    i = 0
    while i < n_iters:
        cycle(lines)
        hash = hashable(lines)
        if (j := history_map.get(hash)) is not None:
            cycle_len = i - j
            left = n_iters - j - 1
            left %= cycle_len

            return history[j + left]

        history_map[hash] = i
        history.append(hash)
        i += 1

    return lines

# Part 1
temp = [line.copy() for line in lines]
move(temp)
print(get_load(temp))

# Part 2
lines = cycle_n_times(lines)
print(get_load(lines))