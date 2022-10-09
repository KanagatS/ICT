# Exercise 23: Area of a Regular Polygon

import math

n, s = map(int, input("Enter n and S: ").split())
area = n * ((s ** 2) / 4 * (math.tan(math.pi / n)))
print("Area =", round(area, 2), "cm^2", sep=" ")
