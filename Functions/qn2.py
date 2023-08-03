'''
Create a function named checkMarks() with argument marks.
Inside the function, check if the user input mark is greater than 70.
If it is greater than or equal to 70, print Pass. Otherwise, print Fail.Outside the function, take user
input for marks.
Call the function using the function name.
Example Input = 90, Expected output Pass
'''

def checkMarks(marks):
    
    if marks >= 70:
        print("pass")
    else:
        print("fail")
try:
    marks = int(input("Enter your mark: "))
except:
    print("Mark should be a number!!")
    marks = int(input("Enter your mark: "))
checkMarks(marks)   
    