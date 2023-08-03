'''
Get an input integer num.
Create a function calculate_pow with a parameter arg1.
Return the result of arg1 raised to the power 3.
Call the function, pass num as its argument, and print the returned value
'''

print("what number do you want to calculate the power!")
try:
    num = int(input("enter a number: "))
    def calculate_pow(arg1):
        return arg1 **3
except ValueError:
    print("Input must be a number or integer")
    num = int(input("enter a number: "))
print(calculate_pow(num))
