'''
Write a program to add an item (entered by the user) to the end of the list.
Create a list named odd_numbers with items 1, 3, and 5.
Take an integer as input and assign it to number variable.
Use the append() function to add user input item to the end of the list.
Print the updated list
'''
odd_numbers = [1,3,5]
print("this is the current list", odd_numbers)
try:
    number = int(input("Enter a number: "))
    odd_numbers.append(number)
    print("This is the updated list",odd_numbers)
except ValueError:
    print("Input must be an integer")
    number = int(input("Enter a number: "))
    odd_numbers.append(number)
    print("This is the updated list",odd_numbers)

