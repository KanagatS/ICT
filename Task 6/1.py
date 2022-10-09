s = input().lower()
vowels = ["a", "o", "y", "e", "u", "i"]

# Removing all vowels from string
for char in vowels:
    s = s.replace(char, "")

# Inserting dot before every consonant and print them
for i in range(len(s)):
    if s[i] not in vowels:
        print("." + s[i], sep="", end="")
