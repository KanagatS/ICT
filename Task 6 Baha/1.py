"""  
Write a string and then print out that string without i-th element in it.

Example:
Input: description: Hello World! Please inter i-th element in string to remove it. 5
Output: description: HelloWorld!  
"""

s = input("Enter string: ")
i = int(input("Position need to delete: "))
print(s.replace(s[i], ""))
