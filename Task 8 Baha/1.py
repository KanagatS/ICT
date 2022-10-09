n = int(input("Enter the number: "))

for i in range(n, 0, -1):
    for num in range(i, 0, -1):
        print(num, end=" ")
    print()
