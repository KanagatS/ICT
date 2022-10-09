nums = [int(i) for i in input().split()]
sm = 0

for num in nums:
    if nums.count(num) == 1:
        sm += num

print(sm)
