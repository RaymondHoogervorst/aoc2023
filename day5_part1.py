import bisect
import fileinput

mappings = [[]]

lines = list(fileinput.input())

for line in lines[2:]:
    line = line.strip()
    if line == '':
        mappings.append([])
    elif line[0].isnumeric():
        vals = map(int, line.split(' '))
        mappings[-1].append(tuple(vals))

for mapping in mappings:
    mapping.sort(key=lambda entry : entry[1])

seeds = list(map(int, lines[0].strip().split(' ')[1:]))

for mapping in mappings:
    starts = [entry[1] for entry in mapping]
    ends = [entry[1] + entry[2] for entry in mapping]
    diffs = [entry[0] - entry[1] for entry in mapping]
    for j, seed in enumerate(seeds):
        i = bisect.bisect_right(ends, seed)
        if i < len(starts) and seed >= starts[i]:
            seeds[j] += diffs[i]

print(min(seeds))

