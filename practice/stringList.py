# Ask the user for a string and print out whether this string is a palindrome or not. (A palindrome is a string that reads the same forwards and backwards.)

# Discussion
# Concepts for this week:

# List indexing
# Strings are lists

import numpy as np

word = input("Please enter a word:")
wordstr = []
str(word)

backword = word[::-1]

if backword == word:
    print("You chose a palindrome!")


else:
    print(backword)



for x in word:
    wordstr.append(x)

rvs = wordstr[::-1]

if rvs == wordstr:
    print("You chose a palindrome!")
else:
    print(rvs)


