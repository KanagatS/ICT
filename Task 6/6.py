s = input()
upper, lower = 0, 0

for i in range(len(s)):
    if s[i].isupper():
        upper += 1
    else:
        lower += 1

if upper == lower or lower > upper:
    print(s.lower())
else:
    print(s.upper())
