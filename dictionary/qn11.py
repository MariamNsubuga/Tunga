'''
Create a function named print_items() that can take any number of arguments.
Inside the function, use a for loop to print all the arguments passed during the function call
Outside the function take two string inputs and store them in variables text1 and text2 respectively
call the print_item() function with text1 as an argument
call the print_item() function with text1 and text2 as arguments
'''
def print_items(*argv):
    for i in argv:
        print(i)
try:
    text1 = input("Enter the first string of your choice: ")
    text2 = input("Enter the second string of your choice: ")
    print_items(text1)
    print_items(text2)
except ValueError:
    print("Inputs must be strings only")
    text1 = input("Enter the first string of your choice: ")
    text2 = input("Enter the second string of your choice: ")
    print_items(text1)
    print_items(text2)
