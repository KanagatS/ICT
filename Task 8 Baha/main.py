output = open("Task 8.txt", "w")

for i in range(1, 6):
    f = open(f"{i}.py", "r")
    output.write(f"Exercise #{i}\n\n")
    output.write(f.read())
    output.write("\n" + str("=" * 90) + "\n\n")

f.close()
output.close()
