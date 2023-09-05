'''
Given a string of size n, check if the string is a palindrome by removing all spaces and special characters.
Use the following Python functions to filter the alphabets and digits in the input string:
isalpha() - returns True if the character is alphabet
isdigit() - returns True if the character is digit
Example Test Input:A man, a plan, a canal: Panama Expected Output:String
is Palindrome
'''
title = "Palindrome program"
r = int(len(title))
print(title.center(r+4,'*'))
def isPalindrome(string):
    rev = reversed(string)
   
    if (list(string) == list(rev)):
        print(string,"is a palindrome word")
    else:
        print(string,"is not a palindrome word")


strings= input("Enter a word: ")
isPalindrome(strings)

