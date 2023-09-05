'''
Write a Python program to find if the given number is a Harshad Number.Harshad Number is any number where the number itself is divisible by the sum of the digits in the
number.
Your program should print,
It is a Harshad Number - if the number is a Harshad Number
It is not a Harshad Number - if the number is not a Harshad Number
Example Test Input:18 Expected Output:It is a Harshad Number
'''
title = "Harshad Number"
r = int(len(title))
print(title.center(r+4,'*'))


result = 0
def harshad_number(n):
    copy_n = n
    while(n != 0):
        digit = n%10
        result =+ digit
        n = n // 10
        # n = int(n/10)
    if (copy_n % result == 0):
        print (copy_n,"is a harshad number")
    else:
        print (copy_n,"is not an harshad number")

number = input("Enter a number: ")
if number.isdigit():
        harshad_number(number)
else:
    print("number must be a digit")
    number = int(input("Enter a number: "))
    harshad_number(number)
