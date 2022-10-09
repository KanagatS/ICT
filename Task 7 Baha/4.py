salary = int(input("Enter ypur salary: "))
year = int(input("Enter ypur year of service: "))

if year > 5:
    print(f"You will get bonus for {salary*0.05} $")
else:
    print("Unfortunately you won't recieve a bonus")
