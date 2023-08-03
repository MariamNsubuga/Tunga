'''
Write a program to print odd integers from a numbers list.
Create a list named numbers with integers 1, 2, 3, 4, 5, 6, 7, 8.
Use a for loop to iterate through numbers.
Inside the loop, print only odd integers
'''

numbers = [1,2,3,4,5,6,7,8]

for i in numbers:
    if i % 2 != 0:
        print(i)
        
