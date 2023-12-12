import fileinput
from functools import lru_cache as cache

@cache
def count_possibilities(springs, groups):

    if not groups:
        if all(c != '#' for c in springs):
            return 1
        else:
            return 0

    first_group, *rest_groups = groups
    minimum_tail = len(rest_groups) + sum(rest_groups)

    possibilities = 0
    for i in range(0, len(springs) - minimum_tail - first_group + 1):


        if all(c != '.' for c in springs[i:i+first_group]):

            if i + first_group == len(springs):
                if len(rest_groups) == 0:
                    possibilities += 1
            elif springs[i+first_group] != '#':
                possibilities += count_possibilities(springs[i+first_group+1:], tuple(rest_groups))

        if springs[i] == '#':
            break

    return possibilities









res1 = 0
res2 = 0

for line in fileinput.input():
    springs, groups = line.strip().split(' ')
    groups = tuple(map(int, groups.split(',')))

    res1 += count_possibilities(springs, groups)

    springs = '?'.join([springs] * 5)
    groups = tuple(groups * 5)

    res2 += count_possibilities(springs, groups)


print(res1)
print(res2)