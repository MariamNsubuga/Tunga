'''
You are given a string that has alphabets, numbers, and special characters.Write a Python program to count the
number of digits in a string.
Example Test Input:The Boys was released in 2019. Expected Output4
'''

# str1 = input("Please Enter your Own String : ")
# alphabets = digits = special = 0

# for i in range(len(str1)):
#     if(ord(str1[i]) >= 48 and ord(str1[i]) <= 57): 
#        digits = digits + 1 
#     elif((ord(str1[i]) >= 65 and ord(str1[i]) <= 90) or (ord(str1[i]) >= 97 and ord(str1[i]) <= 122)):
#         alphabets = alphabets + 1
#     else:
#         special = special + 1
        
# print("\nTotal Number of Alphabets in this String :  ", alphabets)
# print("Total Number of Digits in this String :  ", digits)
# print("Total Number of Special Characters in this String :  ", special)


def count_digits(n):
    alphabets = digits = special = 0
    for i in range(len(n)):
        if(n[i].isalpha()):
            alphabets = alphabets + 1
        elif(n[i].isdigit()):
            digits = digits + 1
        else:
            special = special + 1
    print("Total Number of Digits in this String :  ", digits)
        

userInput=input("Enter a word: ")
count_digits(userInput)
