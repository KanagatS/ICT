import string

alphabet = string.ascii_lowercase

n = int(input())
s = input().lower()

if len(set(s)) == len(alphabet):
    print("YES")
else:
    print("NO")
