import fileinput



def solve(directions, distances):
    prev_point = (0, 0)
    area = sum(distances)

    for direction, distance in zip(directions, distances):
        y, x = prev_point
        if direction == 'L':
            x -= distance
        elif direction == 'R':
            x += distance
        elif direction == 'U':
            y += distance
        else:
            y -= distance

        area += prev_point[0] * x - prev_point[1] * y
        prev_point = (y, x)
    
    return area // 2 + 1

p1_directions = []
p2_directions = []

p1_distances = []
p2_distances = []


hex_to_dir = {
    '0': 'R',
    '1': 'D',
    '2': 'L',
    '3': 'U'
}

for line in fileinput.input():
    direction, distance, hex_code = line.split()

    p1_directions.append(direction)
    p1_distances.append(int(distance))

    p2_distances.append(int(hex_code[2:7], 16))
    p2_directions.append(hex_to_dir[hex_code[7]])

print(solve(p1_directions, p1_distances))
print(solve(p2_directions, p2_distances))