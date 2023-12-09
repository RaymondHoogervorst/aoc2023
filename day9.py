import fileinput

part1 = 0
part2 = 0
for line in fileinput.input():
    nums = list(map(int, line.strip().split(' ')))

    i = 0
    while any(n != 0 for n in nums):
        part1 += nums[-1]
        part2 += nums[0] if i % 2 == 0 else -nums[0]

        i += 1
        nums = [nums[i+1] - nums[i] for i in range(len(nums) - 1)]


print(part1)
print(part2)