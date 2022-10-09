# Exercise 9: Units of Time

d = int(input("Day: "))
h = int(input("Hours: "))
m = int(input("Minutes: "))
s = int(input("Seconds: "))

total = s + (m * 60) + (h * 3600) + (d * 24 * 60 * 60)

print("Total time in seconds:", int(total), "sec", sep=" ")