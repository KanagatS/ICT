total = int(input("Enter classes held: "))
attented = int(input("Enter classes attended: "))

percent = int(100 * attented / total)

if percent >= 75:
    print(f"You allowed to exams, you have {percent}% attendance")
else:
    print("You aren't allowed to exams, your attendance is less than 75%")
