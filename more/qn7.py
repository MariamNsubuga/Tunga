'''
Write a program to find if the given number is an Armstrong Number.
An Armstrong number (for a 3-digit number) is a number where the sum of the cube of
each digit is equal to the original number.
Your program should print,
It is an Armstrong Number - if the number is Armstrong Number
It is not an Armstrong Number - if the number is not Armstrong Number
Example Test Input 371 Expected Output: It is an Armstrong Number
'''
title = "Armstrong Number"
r = int(len(title))
print(title.center(r+10,'*'))
# sum = 0

# def armstrong(num):
#     temp = num
#     while(temp > 0):
#         digit = temp%10
#         sum =+ digit ** 3
#         temp = temp // 10
#         # n = int(n/10)
#     if (num  == sum):
#         print (num,"is a armstrong number")
#     else:
#         print (num,"is not an armstrong number")

# number = int(input("Enter a number: "))
# armstrong(number)
# if number.isdigit(): 
        
#         armstrong(number)
# else:
#     print("number must be a digit")
#     number = int(input("Enter a number: "))
#     armstrong(number)
sum = 0

num = int(input("Enter a number: "))
temp = num
while(temp > 0):
    digit = temp % 10
    sum += digit ** 3
    temp = temp // 10
    # n = int(n/10)
if (num  == sum):
    print (num,"is a armstrong number")
else:
    print (num,"is not an armstrong number")


