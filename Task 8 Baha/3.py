numbers = [int(num) for num in input("Numbers: ").split(" ")]

for num in range(len(numbers)):
    if numbers[num] % 3 == 0:
        if numbers[num] <= 120:
            print(numbers[num])
        elif numbers[num] > 300:
            break
        else:
            continue
