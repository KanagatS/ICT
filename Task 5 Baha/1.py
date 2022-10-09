# Exercise 1: Bottle Deposits

containers = map(int, input().split())
jurisdiction = 0

for elem in range(len(containers)):
    if containers[elem] <= 1:
        jurisdiction += 0.1
    elif containers[elem] > 1:
        jurisdiction += 0.25

print(f"Total jurisdiction = {jurisdiction} $")
