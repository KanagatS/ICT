cost = int(input("Count of purchases: "))
total = cost * 100

if total >= 1000:
    print(f"You'll get discount 10%, and total cost is {int(total - total * 0.1)} $")
else:
    print(f"You won't get discount, total cost is {total} $")
