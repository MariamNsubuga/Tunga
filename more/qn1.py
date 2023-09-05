'''
Create a Python program to find the total number of special characters in a string. Use the following inbuilt Python
functions:
'''
def check(a):
     # printing original string
    print("The original string is : " + a)

# using split()
# to count words in string
    results = len(a.split())

# printing result
    print("The number of words in string are : " + str(results))
    print("The number of words in string are : ", len(a))

ch = input("Please enter words or characters:")

check(ch)

