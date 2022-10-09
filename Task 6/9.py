n = int(input())
s = input()

Anton, Danik = s.count("A"), s.count("D")

if Danik > Anton:
    print("Danik")
elif Anton > Danik:
    print("Anton")
else:
    print("Friendship")
