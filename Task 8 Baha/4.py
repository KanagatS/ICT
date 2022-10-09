start = int(input("Enter starting number: "))
end = int(input("Enter ending number: "))

print(f"Prime numbers between {start} and {end} are: ")

for num in range(start, end + 1):
    for i in range(2, num // 2):
        if num % i == 0:
            break
        else:
            print(num)
            break
