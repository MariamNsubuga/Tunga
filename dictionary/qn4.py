'''
Define a function named full_name() with two arguments first_name and last_name.
Inside the function, print first_name and last_name and separate them by an empty space.
Outside the function, take string input for first name and last name and assign them to first and last
variables.
Call the function and pass first and last as arguments.
'''

def full_name(first_name, last_name):
    print(first_name, ' ', last_name)


first_name = input("What is your first name?: ")
last_name = input("What is your last name?: ")
if first_name and last_name != str:
    print("First and last name must be strings!! ")
    first_name = input("What is your first name?: ")
    last_name = input("What is your last name?: ")

full_name(first_name, last_name)