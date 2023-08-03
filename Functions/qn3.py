'''
Get two integer inputs num1 and num2.
Create a function my_function() that accepts two arguments.
Inside the function, check to see if the two arguments are equal.
If they are equal, return True, else return False.
Call the function, pass integers num1 and num2 as arguments to the function, and print the
returned value.
Example Input = 1 2, Expected output Fals
'''

try:
    num1 = int(input("Enter first number you want to compare: "))
    num2 = int(input("Enter second number you want to compare: "))

except:
    print("first and second numbers must be numbers or integers!!")
    num1 = int(input("Enter first number you want to compare: "))
    num2 = int(input("Enter second number you want to compare: "))

def my_function(num1, num2):
    if num1 == num2:
        return True
    else:
        return False
print(my_function(num1, num2))