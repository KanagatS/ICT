output = open("Task 6.txt", "w")

for i in range(1, 13):
    f = open(f"{i}.py", "r")
    output.write(f"Exercise {i} \n\n")
    output.write(f.read())
    output.write("\n\n" + 90 * "=" + "\n\n")

f.close()
output.close()
