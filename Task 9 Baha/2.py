nums = [int(i) for i in input().split()]
cnt = 0

for i in range(len(nums)):
    for j in range(len(nums)):
        if i != j and nums[i] > nums[j]:
            cnt += 1
    print(cnt, end=" ")
    cnt = 0
