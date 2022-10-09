mark = int(input("Enter your total score: "))

if mark < 25:
    print("Your mark is F")
elif 25 <= mark < 45:
    print("Your mark is E")
elif 45 <= mark < 50:
    print("Your mark is D")
elif 50 <= mark < 60:
    print("Your mark is C")
elif 60 <= mark < 80:
    print("Your mark is B")
else:
    print("Your mark is A")
