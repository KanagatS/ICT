""" 
Program to check if the “word” entered by user is present in the "sentence".

Example:
Input: description : text: Hello world!
word: Hello
Output: description: True 
"""

text = input("Enter string: ").split()
word = input("Enter word: ")

if word in text:
    print("True")
else:
    print("False")
