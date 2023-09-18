'''
Write a Python program that checks whether the given number is Lapindrome or not.
A Lapindrome Number is a number, which when split in the middle, gives two halves having the
same characters and the same frequency of each character.
The numbers can be split in the middle whether or not the number has an odd number of digits.
Your program should print,
It is Lapindrome Number - when the number is Lapindrome
It is not Lapindrome Number - when the number is not Lapindrome
Assumption: We will assume the passed integer will only be positive.
Example Test Input:1234321 Expected Output:It is Lapindrome Number
'''



def lapindrome(x):
    l = int(len(x)/2)
    if sorted(x[:l]) == sorted(x[-l:]):
        print("yes")
    else:
        print("no")
userInput = input("enter something: ")
lapindrome(userInput)