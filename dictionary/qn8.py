'''
Define a function named find_sum() that takes n as an argument.
Inside the function, compute the sum of numbers from 1 to n and return the total.
Outside the function, get an integer input for a variable number.
Call the function and pass number as an argument and print the return value.
'''
def find_sum(n):
    sum = 0
    for i in range (1,n+1):
        
        sum+= i
        print (sum)
try:
    number = int(input("Enter a number: "))
    find_sum(number)
except ValueError:
    print("Input must be a digit")
    number = int(input("Enter a number: "))
    find_sum(number)
    
