'''
Create a function named display_info().
This function must accept two arguments: name and location.
Print name and location in two separate lines. 2. Step 2
Outside of the function:
Get string input from the user and assign it to the country variable.
Call the display_info() with arguments: the "Magnus" string and the country variable,
respectively.
'''

def display_info(name, location):
    
    
    print (name, "\n", location)


n =input("what is your name?: ")
l =input("waht is your location?: ")
country = input("what is your country? ")
if  str.isalpha(n and l and country):
    display_info("Magnus",country) 
else:
    print("All inputs must be strings")
    
