pos = int(input("Enter pos: "))
s = input("Enter string: ")

print("".join([i for i in s if (s.index(i) < pos) and i.isalpha()]), end="")
print(s[pos:])
