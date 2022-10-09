N = int(input())
s = input()

z = s.count("z")
e = s.count("e")
r = s.count("r")
o = s.count("o")
n = s.count("n")

while True:
    if o > 0 and n > 0 and e > 0:
        print(1, end=" ")
        o -= 1
        n -= 1
        e -= 1
    else:
        break

while True:
    if z > 0 and e > 0 and r > 0 and o > 0:
        print(0, end=" ")
        z -= 1
        e -= 1
        r -= 1
        o -= 1
    else:
        break
