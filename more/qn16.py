'''
An intern at a company followed the camelCase convention while writing codes. But the company has been using
snake_case for a long time.Now, write a Python program that converts camelCase strings to snake_case.
Assumption: We will assume that input and output data types are strings.
Example Test Input helloWorld Expected Output:hello_world
'''

def change_case(x):
    
    return ''.join(['_'+i.lower() if i.isupper()
               else i for i in x]).lstrip('_')

userInput =input("Enter a word to be converted to snake case: ") 
print(change_case(userInput))

