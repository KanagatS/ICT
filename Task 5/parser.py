""" Due to the fact that I had 11 tasks, I got 11 python files. 
But in teams assigment you can upload 10 files maximum. 
And I decided to write a parser to collect all tasks in one file. """

output = open("Task 5.txt", "w")

for i in range(1, 12):
    f = open(f"{i}.py", "r")
    output.write(f.read())
    separator = "\n\n" + str(90 * "=") + "\n\n"
    output.write(separator)

f.close()
output.close()
