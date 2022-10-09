age = int(input("Age: "))
sex = input("Sex (M/F): ")
status = input("Status (Y/N): ")

if sex == "F":
    print("She will work only in urban areas")
elif sex == "M":
    if 20 <= age < 40:
        print("He can work in anywhere")
    elif 40 <= age < 60:
        print("He will work in urban areas only")
else:
    print("ERROR")
