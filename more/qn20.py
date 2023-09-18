'''
Given a list of numbers that are already in ascending order, square the numbers.But the result should be in ascending order as well
Assumption: The input numbers are always in ascending order.
Example Test Input -7 -2 0 4 5, 7Expected Output [0, 4, 16, 25, 49, 49]
'''

def square(x):
#    y = list(x)
   y =[int(x) for x in input().split()]
   squared= [ i ** 2 for i in y]
   results = squared.sort()
   print(results)
userInput = (input("Enter a number: "))
square(userInput)

# def squarenumber():
#   num = raw_input('Enter numbers, eg 1,2,3: ').split(',')
#   print [int(n) for n in num if n.isdigit()]  ##display user input
#   lst = []
#   for n in num:
#     if n.isdigit():
#       nn = int(n)
#       lst.append(nn*nn)
#   print lst
#   return lst  

# x = squarenumber()