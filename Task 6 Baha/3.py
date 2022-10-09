""" 
Program to find the length of the string

Example:
Input: description : Hello world!
Output: description: 11 
"""

s = input("Enter string: ")
space = len([i for i in range(len(s)) if s[i] == " "])
print("Length of string: ", len(s) - space, sep=" ")
