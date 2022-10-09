""" 
Program to print even length words in python. If the words are not even don’t print them.

Example:
Input: description: Hi World again
Output: description: Hi
"""

s = input("Enter string: ").split()
print(*[s[i] for i in range(len(s)) if len(s[i]) % 2 == 0])
