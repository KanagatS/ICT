nums = [int(i) for i in input().split()]
cnt = len(nums) // 2

for num in nums:
    if nums.count(num) == cnt:
        print(num)
        break
