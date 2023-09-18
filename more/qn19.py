'''
Given a string, only reverse the words that have an odd length of characters in a string.
But if the length of the word is even, leave the word as it is.
Your program should print the semi-reversed string.
Example Test Input Learn to code from Programiz Expected Output nraeL to code
from zimargorP
'''

def test(txt):
	return ' '.join(i[::-1] if len(i)%2 else i for i in txt.split())
 
userInput=input("Enter a word: ")
print(test(userInput))