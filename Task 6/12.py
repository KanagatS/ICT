n = int(input())
s = input()
cnt = 0

while s.find("xxx") != -1:
    s = s.replace("x", "", 1)
    cnt += 1

print(cnt)
