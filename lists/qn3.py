'''
Write a program to calculate the product of list items.
Create a list my_list and assign [2, 5, 3, 4, 1] to it.
Declare a variable product with value 1.
Iterate over my_list and multiply each item to product.
Print product
'''

my_list = [2,5,3,4,1]

product = 1
for i in my_list:
    product *= i
    print ("The product of this list",my_list,"is",product)

