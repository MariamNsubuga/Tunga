'''
Write a Python program that takes two integer parameters and checks if the sum of digits in each parameter is
equal.
Your program should print,
True - if the sum of digits in both parameters are the same
False - if the sum of digits in both parameters are different
Example
Test Input 243 900
Expected Output True
'''

def getSum(n,m):
    
    sum = 0
    sum1 = 0
    for digit in str(n): 
        sum += int(digit)      
    for digits in str(m):
        sum1 += int(digits)   
    if sum == sum1:
        print("True, the sum of the above numbers is the same")
    else:
        print("False, the sum of the above numbers is the different")
        
   
userInput=int(input("enter anumber: "))
userInput1=int(input("enter anumber: "))
getSum(userInput,userInput1)