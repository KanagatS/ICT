n = int(input("Enter number: "))

if n == 1:
    print(0)

else:
    print("Fibonacci sequence:")

    n1, n2, cnt = 0, 1, 0

    while cnt < n:
        print(n1, end=" ")
        f = n1 + n2
        n1 = n2
        n2 = f
        cnt += 1
