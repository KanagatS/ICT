# Exercise 25: Units of Time (Again)

t = int(input("Seconds: "))

h = (t // 3600) % 24
m1 = t // 60 % 60 // 10
m2 = t // 60 % 60 % 10
s1 = t % 60 // 10
s2 = t % 10

print("Time is: ", end="")
print(h, ":", m1, m2, ":", s1, s2, sep="")
