# Exercise 28: Wind Chill

t, v = map(int, input("Enter temperature and velocity of wind: ").split())

if t <= 10 and v > 4.8:
    WCI = 13.12 + 0.6215 * t - 11.37 * (v ** 0.16) + 0.3965 * t * (v ** 0.16)
    print("WCI =", int(WCI), sep=" ")
else:
    print("Input isn't correct D:")
