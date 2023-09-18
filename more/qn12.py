'''
Write a program to find if the passed number is an Abundant Number.
An abundant number is any number whose proper factors' sum is greater than the number
itself.
Your program should print,
It is an Abundant Number - if the number is Abundant Number
It is not an Abundant Number - if the number is not Abundant Number
Example Test Input:18 Expected Output:It is an Abundant Number
'''

def abundant_number(n):
    for i in range(1,n):
        if n%i ==0:
            s=0
            s+= i
    if s <n:
        print("Abundant Number")
    else:
        print("Not abundant Number")

userInput = int(input("Enter a number: "))
abundant_number(userInput)