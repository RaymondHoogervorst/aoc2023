import fileinput


grid = [line.strip() for line in fileinput.input()]

height = len(grid)
width = len(grid[0])

points = []

for row in range(height):
    for col in range(width):
        if grid[row][col] == '#':
            points.append((row, col))


def solve(expansion_rate):
    col_distances = [0] * width
    for col in range(width):
        if all(grid[i][col] == '.' for i in range(height)):
            col_distances[col] = col_distances[col - 1] + expansion_rate
        else:
            col_distances[col] = col_distances[col - 1] + 1

    row_distances = [0] * height
    for row in range(height):
        if all(grid[row][i] == '.' for i in range(width)):
            row_distances[row] = row_distances[row - 1] + expansion_rate
        else:
            row_distances[row] = row_distances[row - 1] + 1

    res = 0
    for i, pointA in enumerate(points):
        for pointB in points[i:]:
            res += abs(col_distances[pointB[1]] - col_distances[pointA[1]]) + abs(row_distances[pointB[0]] - row_distances[pointA[0]])
    
    return res

print(solve(2))
print(solve(1_000_000))