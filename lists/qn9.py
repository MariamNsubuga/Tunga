'''
Given a list of numbers that are already in ascending order, square the numbers.
But the result should be in ascending order as well
Assumption: The input numbers are always in ascending order.
Example Test Input -7 -2 0 4 5, 7Expected Output [0, 4, 16, 25, 49, 49]
'''
try:
    
    test = list(map(int,(input("Enter numbers you want to find squares for: ").split(','))))
    print("This is your list: ",test)
    s= [i**2 for i in test]
    s.sort()
    print("this is the sorted square list", s)
except ValueError:
    print("Inputs should be integers and numbers")