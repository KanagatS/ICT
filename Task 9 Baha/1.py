nums = [int(i) for i in input().split()]
count = 0

for i in range(len(nums)):
    for j in range(i + 1, len(nums)):
        if nums[i] == nums[j]:
            count += 1

print(count)