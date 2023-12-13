import fileinput

lines = [line.strip() for line in fileinput.input()] + [""]

def diff(a, b):
    return sum(a[i] != b[i] for i in range(len(a)))

def solve1(rows):
    n = len(rows)
    m = len(rows[0])
    rows = list(map(tuple, rows))
    cols = [tuple(rows[i][j] for i in range(n)) for j in range(m)]

    for i in range(1, m):
        for r in range(min(m - i, i)):
            if cols[i+r] != cols[i-1-r]: break
        else:
            return i

    for i in range(1, n):
        for r in range(min(n - i, i)):
            if rows[i+r] != rows[i-1-r]: break
        else:
            return i * 100

    assert False, "No reflection"


def solve2(rows):
    n = len(rows)
    m = len(rows[0])
    rows = list(map(tuple, rows))
    cols = [tuple(rows[i][j] for i in range(n)) for j in range(m)]

    for i in range(1, m):
        total_diff = sum(diff(cols[i+r], cols[i-1-r]) for r in range(min(m - i, i)))
        if total_diff == 1:
            return i

    for i in range(1, n):
        total_diff = sum(diff(rows[i+r], rows[i-1-r]) for r in range(min(n - i, i)))
        if total_diff == 1:
            return i * 100

    assert False, "No reflection"

res1 = 0
res2 = 0
last_gap = -1
for i, line in enumerate(lines):
    block = lines[last_gap+1:i]

    if line == "":
        # res1 += solve1(lines[last_gap+1:i])
        res2 += solve2(lines[last_gap+1:i])
        last_gap = i

# print(res1)
print(res2)