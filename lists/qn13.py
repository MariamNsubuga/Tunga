'''
Write a program to concatenate two strings.
Get two string inputs for variables string1 and string2.
Concatenate these strings and store them in the result variable.
Print the value of result
'''
try:
    string1 = input("Enter first string: ")
    string2 = input("Enter second string: ")
    result = string1 + string2
    print(result)
except:
    print("Inputs must be strings")