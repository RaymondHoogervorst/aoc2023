from collections import OrderedDict
import fileinput

line = next(fileinput.input())
steps = line.split(',')

def hash(step):
    res = 0
    for c in step:
        res = ((res + ord(c)) * 17) % 256
    return res

# Part 1
print(sum(map(hash, steps)))

# Part 2
boxes = [OrderedDict() for _ in range(256)]

for step in steps:
    if step[-1] == '-':
        label = step[:-1]
        box = boxes[hash(label)]
        if label in box: box.pop(label)
    else:
        label, value = step.split('=')
        box = boxes[hash(label)]
        box[label] = int(value)

print(sum((i + 1) * (j + 1) * value for j, box in enumerate(boxes) for i, value in enumerate(box.values())))