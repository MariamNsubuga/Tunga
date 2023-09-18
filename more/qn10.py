'''
Given a list of numbers, find the sums of even numbers and odd numbers.
Print both sums in a tuple as (odd_sum, even_sum).
Assumption: We will assume the list contains only numbers.
Example Test Input:51 75 69 36 75 44 82 36 Expected Output:```(270, 198)
'''

# def sum_of_numbers(x):
#     # y=list(x)
    
#     # for i in  range (0,len(x)):
#     for i in range (x[0],x[-1]):
#         for y in x[i]:
#             if y % 2 ==0:
#                 even_sum = 0
#                 even_sum += y
#             else:
#                 old_sum = 0
#                 old_sum += y
#     result = (old_sum, even_sum)

#     print("Sum of old, even is", tuple(result) )
       
# userInput= input("Enter numbers: ")
# sum_of_numbers(userInput)
Even_Sum = 0
Odd_Sum = 0

num_list = [51,75,69,36,75,44 ,82, 36]

# Print the Original List
print("Original List: ", num_list)

for j in range(len(num_list)):
    if(num_list[j] % 2 == 0):
        Even_Sum = Even_Sum + num_list[j]
    else:
        Odd_Sum = Odd_Sum + num_list[j]
result = (Even_Sum, Odd_Sum)

print("\nThe Sum of Even Numbers  and Odd Numbers in the Given List =  ", tuple(result))
