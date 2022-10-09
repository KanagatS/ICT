nums = [int(i) for i in input().split()]

# We'll use dictionary to calculate count of every number
d, t = {}, {}
for num in nums:
    if num not in d:
        d[num] = 1
    else:
        d[num] += 1

for v in d.values():
    if v in t:
        print("False")
        break
    t[v] = 1

else:
    print("True")
