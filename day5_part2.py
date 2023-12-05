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

seeds = list(map(int, lines[0].split(' ')[1:]))
n = len(seeds)
seeds = [(seeds[i], seeds[i] + seeds[i+1]) for i in range(0, n, 2)]

for mapping in mappings:
    starts = [entry[1] for entry in mapping]
    ends = [entry[1] + entry[2] for entry in mapping]
    diffs = [entry[0] - entry[1] for entry in mapping]

    m = len(mapping)

    new_seeds = []

    for begin, end in seeds:
        i = bisect.bisect_right(ends, begin)

        while i < m and begin < end:
            if begin < starts[i]:
                new_seeds.append((begin, starts[i]))
                begin = starts[i]
            else:
                local_end = min(end, ends[i])
                new_seeds.append((begin + diffs[i], local_end + diffs[i]))
                begin = local_end
                i += 1
        if begin < end:
            new_seeds.append((begin, end))

    seeds = new_seeds

print(min(seeds)[0])

