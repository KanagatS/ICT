s = input()

if s[0].islower() or s == s.lower():
    print(s.lower().capitalize())
else:
    print(s)
