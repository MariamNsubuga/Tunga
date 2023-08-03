'''
Create a program to print the occurrence of a character in the string.
Take string input and store it in the string1 variable.
Take a character input (a string with a single character) and store it in character1 variable.
Create a variable named count and initialize it to 0.
Use a for loop to iterate through string1.
Inside the loop, check the occurrence of the character in the string. If it's True, increment count by 1.
Print the count variable.
'''
print("program to print the occurrence of a character in the string.")
print("---------------------------------------------")
try:
    string1 =  input("Enter a string: ")
    character1 = input("Enter a character: ")
    count = 0
    for i in string1:
        if i == character1:
            count += 1      
    print(count)
except:
    print("input should be strings only")