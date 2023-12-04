import fileinput

sum = 0

valid_digit_strings = {
    '1': 1,
    '2': 2,
    '3': 3,
    '4': 4,
    '5': 5,
    '6': 6,
    '7': 7,
    '8': 8,
    '9': 9,

    'one': 1,
    'two': 2,
    'three': 3,
    'four': 4,
    'five': 5,
    'six': 6,
    'seven': 7,
    'eight': 8,
    'nine': 9,
}


for line in fileinput.input():
    n = len(line)

    # Find the first digit
    i = 0
    while i < n:
        for string, val in valid_digit_strings.items():
            if i + len(string) <= n and line[i:i+len(string)] == string:
                sum += val * 10
                i += len(string)
                break
        else:
            i += 1
            continue
        break

    # Find the last digit
    i = n
    while i >= 0:
        for string, val in valid_digit_strings.items():
            if i - len(string) >= 0 and line[i-len(string):i] == string:
                sum += val
                i -= len(string)
                break
        else:
            i -= 1
            continue
        break


print(sum)