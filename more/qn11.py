'''
Write a Python program to count the number of characters that occur more than once in a string.
Assumption: We will assume that uppercase and lowercase letters (such as P and p) are the
same. Also, special characters are not counted.
Example Test Input:"Nick Fury Hired Iron Man." Expected Output:3
'''

import collections


def count_words(x):
    print(collections.Counter(x).most_common()[0])
userInput = input("Enter words to be counted: ")
count_words(userInput)

