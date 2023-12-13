import fileinput

lines = [line.strip() for line in fileinput.input()] + [""]

def diff(a, b):
    return sum(a[i] != b[i] for i in range(len(a)))

def solve(rows, diff_target=0):
    n = len(rows)
    m = len(rows[0])
    rows = list(map(tuple, rows))
    cols = [tuple(rows[i][j] for i in range(n)) for j in range(m)]

    for i in range(1, m):
        if sum(diff(cols[i+r], cols[i-1-r]) for r in range(min(m - i, i))) == diff_target:
            return i

    for i in range(1, n):
        if sum(diff(rows[i+r], rows[i-1-r]) for r in range(min(n - i, i))) == diff_target:
            return i * 100

res1 = 0
res2 = 0
last_gap = -1
for i, line in enumerate(lines):
    if line == "":
        block = lines[last_gap+1:i]
        res1 += solve(block)
        res2 += solve(block, 1)
        last_gap = i

print(res1)
print(res2)