'''
Given the height and weight of a person, calculate the BMI and alert the user about what they should do next.
BMI is a number that tells how fit the human body is. It depends on height and weight. Write a
Python program that takes weight (in kgs) and height (in meters) then calculates the BMI using this
formula,
BMI = weight / height2
Your program should print the given string if the BMI is,
less than 18.5 - Underweight
18.5 to 24.9 - Normal Weight
25.0 to 29.9 - Overweight
30.0 or more - Obese
Example Test Input 65 1.67 Expected Output:Normal Weight
'''

def calculate_height(weight,height):
    BMI = weight / height

    if BMI < 18.5:
        print("Underweight")
    elif BMI> 18.5 or BMI < 24.9:
        print("Normal weight")
    elif BMI > 25 or BMI<29.9:
        print("Overweight")
    elif BMI>30:
        print("obese")

userInput = float(input("What is your weight: "))
userInput1 = float(input("What is your height: "))
calculate_height(userInput,userInput1)  