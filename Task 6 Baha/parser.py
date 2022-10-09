output = open("Task 6.txt", "w")

for i in range(1, 6):
    f = open(f"{i}.py", "r")
    output.write(f.read())
    separator = "\n\n" + str(90 * "=") + "\n\n"
    output.write(separator)

f.close()
output.close()
