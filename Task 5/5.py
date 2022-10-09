# Exercise 13: Making Change

print("Coffee machine can take only 5, 10, 20, 50, 100 tenge coins")
entered = int(input("How much you entered: "))
cost = int(input("how much is your drink worth? "))

print(f"Your change are {entered - cost}")
