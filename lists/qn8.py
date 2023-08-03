'''
Given a list of numbers, find the sums of even numbers and odd numbers.
Print both sums in a tuple as (odd_sum, even_sum).
Assumption: We will assume the list contains only numbers.
Example Test Input:51 75 69 36 75 44 82 36 Expected Output:```(270, 198)
'''

evenOddTuple = (51,75, 69, 36, 75, 44, 82, 36)
print("Even and Odd Tuple Items = ", evenOddTuple)

tEvenSum = tOddSum = 0
for i in evenOddTuple:
    if(i % 2 == 0):
        tEvenSum = tEvenSum + i
    else:
        tOddSum = tOddSum + i

print("odd_sum = ", tEvenSum, "even_sum = ",tOddSum)
