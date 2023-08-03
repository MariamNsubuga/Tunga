'''Given a list of numbers, find if the list elements are in ascending sequence or not a sequence at all. Write a
Python program that prints,
True - if the list elements are a perfect sequence
False - if the list elements are not a sequence
Example Test Input 1 2 3 4 5 Expected Output True'''

try:
    
    test = list(map(int,(input("Enter numbers you want to check if the list is sorted: ").split(','))))
    print("This is your list: ",test)
    flag = 0
    i = 1
    while i < len(test):
        if(test[i] < test[i - 1]):
            flag = 1
        i += 1
        
    
    if (not flag) :
        print ("Yes, List elements are a perfect sequence")
    else :
        print ("No, List elements are not a sequence.")
except ValueError:
    print("Inputs should be integers and numbers")