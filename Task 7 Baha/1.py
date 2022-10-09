size = input("Size: ")
add = input("Add pepperoni? (Yes/No) ")
cheese = input("You want extra cheese? (Yes/No) ")

bill = 0

if size == "L":
    bill += 25
elif size == "M":
    bill += 20
else:
    bill += 15

if add == "Yes":
    if size == "S":
        bill += 2
    else:
        bill += 3

if cheese == "Yes":
    bill += 1

print(f"Your final bill: {bill} $")
