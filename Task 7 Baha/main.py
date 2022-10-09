output = open("Task 7.txt", "w")

for i in range(1, 11):
    f = open(f"{i}.py", "r")
    output.write(f"Exercise #{i}\n\n")
    output.write(f.read())
    separator = "\n\n" + str(90 * "=") + "\n\n"
    output.write(separator)

f.close()
output.close()
