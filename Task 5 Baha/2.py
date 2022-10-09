# Exercise 2: Tax and Tip

cost = int(input("Cost: "))
tip, tax = cost * 0.18, cost * 0.3
print(f"Tip will be {round(tip, 2)} tenge \nTax will be {round(tax, 2)} tenge")
print(f"Total amount is {round(cost+tip+tax,2)} tenge")
