'''
A prime number is a number that is only divided by either 1 or itself. For example, 7, 5, 19, etc.
Define a function named check_prime().
Inside the function, create a variable named num
if num is prime number, print Prime Number. Otherwise, print Not Prime Number.
Outside the function, get an integer input for the number variable.
Call the function and pass number as an argument
'''

def check_prime(num):
    if num <= 1:
        return False
    for i in range (2, num):
        if num % i == 0:
            return False
    return True

try:
    number = int (input("What number do you want to check if its prime?"))
except ValueError:
    print("Input must be number or integers only")
    number = int (input("What number do you want to check if its prime?"))
if check_prime(number):
    print(number, "is a prime number")
else:
    print(number, "is not a prime number")