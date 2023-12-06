import fileinput
import math

def margin(time, record):

    # x * (time - x) = record
    # x^2 - time * x + record = 0

    D = math.sqrt(time * time - 4 * record)
    lower = (time - D) / 2
    upper = (time + D) / 2

    lower = math.floor(lower)
    upper = math.ceil(upper)

    return upper - lower - 1

lines = [line.strip() for line in fileinput.input()]

times, records = ([int(token) for token in line.split(' ')[1:] if token] for line in lines)

res1 = 1
for time, record in zip(times, records):
    res1 *= margin(time, record)

print(res1)

time, record = (int(''.join(line.split(' ')[1:])) for line in lines)

print(margin(time, record))