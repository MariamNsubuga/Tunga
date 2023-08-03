'''
Give default value 5 to argument a and 10 to argument b.
Inside the function, print a and b in two separate lines.
Outside of the function
Take integer input and assign it to variable n.
Call the call_me() function with n as an argumen
'''
a,b = 5,10

def call_me(a=5,b=10):
        print(a,"\n",b)
try:
    n = int(input("Enter an interger: "))
    
    call_me(n)
except ValueError:
    print("Input must be an integer!!")
    n = int(input("Enter an interger: "))
    call_me(n)