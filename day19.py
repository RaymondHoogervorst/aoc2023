import fileinput

lines = [line.strip() for line in fileinput.input()]

i = lines.index('')
rulesets = lines[:i]
items = lines[i + 1:]

ruleset_map = {}

for ruleset in rulesets:
    label, rules = ruleset[:-1].split('{')
    rules = [rule.split(':') for rule in rules.split(',')]
    
    ruleset_map[label] = rules

# Part 1
res1 = 0
for item in items:
    values = [int(value[2:]) for value in item[1:-1].split(',')]
    x, m, a, s = values

    state = 'in'

    while state != 'A' and state != 'R':
        rules = ruleset_map[state]

        for condition, next_state in rules[:-1]:
            if eval(condition.format(x=x, m=m, a=a, s=s)):
                state = next_state
                break
        else:
            state = rules[-1][0]

    if state == 'A':
        res1 += sum(values)
print(res1)

# Part 2
from functools import cache


MAX_VAL = 4000

def solve(state, limits):
    
    if state == 'R':
        return 0

    if state == 'A':
        prod = 1
        for lower, upper in limits.values():
            prod *= upper - lower + 1
            
        return prod
    


    rules = ruleset_map[state]
    res = 0

    for rule, dst in rules[:-1]:
        var = rule[0]
        operator = rule[1]
        value = int(rule[2:])

        lower, upper = limits[var]
        if operator == '>':
            if upper > value:
                new_limits = dict(limits, **{var : (max(lower, value+1), upper)})
                res += solve(dst, new_limits)

            if upper > value:
                upper = value

        else:
            if lower < value:
                new_limits = dict(limits, **{var : (lower, min(upper, value-1))})
                res += solve(dst, new_limits)

            if lower < value:
                lower = value

        limits.update({var : (lower, upper)})
    
    return res + solve(rules[-1][0], limits)


limits = {c : (1, MAX_VAL) for c in 'xmas'}

print(solve('in', limits))