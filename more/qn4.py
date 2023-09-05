'''
Suppose you are in a restaurant with your friends. You get a bill of a certain amount.
If the tax rate is 8.875%, find out how much should each of you pay equally.
Note: Get user input for the bill amount and the total number of people paying the bill.
Example Test Input: 300 6 Expected Output: 54.4375
'''
title = "Bill calculator"

print(title.center(30,'*'))
def bill_tax(amount, people):
    tax = 8.875 / 100
    bill_before_tax = amount * tax
    bill_after_tax = bill_before_tax + amount
    total_bill = bill_after_tax / people
    print("Each person will pay", total_bill)

cash = float(input("Enter total bill: "))

number_of_people = int(input("how many are you? "))

bill_tax(cash,number_of_people)
