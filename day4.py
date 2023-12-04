import fileinput

lines = [line.strip() for line in fileinput.input()]
n = len(lines)

def parse(nums):
    return [int(nums[i:i+2]) for i in range(0, len(nums), 3)]

def get_value(line):
    line = line.strip().split(': ')[1]
    winning, nums = map(parse, line.split(' | '))

    n_matching = len(set(winning).intersection(nums))
    
    return 2 ** (n_matching - 1) if n_matching > 0 else 0, n_matching
    # else:
        

results = [get_value(line) for line in lines]

# Part 1
print(sum(map(lambda x: x[0], results)))

# Part 2
for i in range(n-1, -1, -1):
    n_matching = results[i][1]
    results[i] = sum(results[i+1:i+1+n_matching]) + 1


print(sum(results))