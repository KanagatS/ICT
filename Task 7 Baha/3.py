w = int(input("Enter your weight: "))
h = float(input("Enter your height: "))

BMI = round(w / (h ** 2))

if BMI < 18.5:
    print(f"Your BMI = {BMI}, you are underweight")
elif 18.5 <= BMI < 25:
    print(f"Your BMI = {BMI}, you have normal weight")
elif 25 <= BMI < 30:
    print(f"Your BMI = {BMI}, you are slightly overweight")
elif 30 <= BMI < 35:
    print(f"Your BMI = {BMI}, you are obese")
else:
    print(f"Your BMI = {BMI}, you are clinically obese")
