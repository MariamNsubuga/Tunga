'''
Write a Python program that returns a string representation of numbers 1 to n.
But instead of numbers that are divisible by 3, it should print Fizz and instead of numbers that are
divisible by 5, it should output Buzz.
Example Test Input: 9 Expected Output: ['1', '2', 'Fizz', '4', 'Buzz', 'Fizz',
'7', '8', 'Fizz']
'''

def numbers(a):
    for i in range(a+1):
        if i%3 ==0:
            print("Fizz")
        elif i%5 ==0:
            print("Buzz")
        else:
            print(i)
number = int(input("Enter a number: "))

numbers(number)