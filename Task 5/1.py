# Exercise 6: Tax and Tip

cost = int(input("Cost of your meal in tenge: "))
tip = cost * 0.18
tax = cost * 0.3
print(f"Tip will be {round(tip, 2)} tg and tax will be {round(tax, 2)} tg")
print(f"Total amount is {round(cost+tip+tax,2)}")
