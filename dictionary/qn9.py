'''
Here's the formula to compute the area of a circle.
Area = 3.14 * radius * radius
Create the compute_area() function that accepts float parameters radius and pi.
Inside the function, compute the area of the circle and return it.
Outside the function, get a float input value for the radius of the circle.
Create a float variable named pi with value 3.14.
Call compute_area() with arguments radius and pi.
Print the returned value.
'''
pi = 3.14
def compute_area(radius,pi):
    Area = pi * radius * radius
    return Area
try:
    radius = float(input("What is the radius of your circle?: "))
    print(compute_area(radius,pi))
except ValueError:
    print("Input value should be anumber ")
    radius = float(input("What is the radius of your circle?: "))
    print(compute_area(radius,pi))
