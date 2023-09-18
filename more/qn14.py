'''
In any given string, repeat the vowel letters up to a given number. Write a Python function that takes a string and
a number, then prints the new string with the repeated vowels in the console.
Example Test Input Pencil:3 Expected Output:Peeenciiil
'''
# sum = 0
# def vowel(a,b):
#     vowel_list = ['a','e','o','i','u']
#     for i in range(0,len(a)):
        
#         if a[i] in  vowel_list:
#             print (a[i]*b)
          
            
# userInput = input("Enter a word: ")
# userInput1 = int(input("Enter number of times you want to repeat the vowels: "))

# vowel(userInput,userInput1)

sum = 0
def vowel(a,b):
    vowel_list = ['a','e','o','i','u']
    res = ""
    for i in range(0,len(a)):
        
        if a[i] in  vowel_list:
            res += a[i]*b
            
        res += a[i]
        
    print("String with Vowels duplicated: ", res)
           
          
            
userInput = input("Enter a word: ")
userInput1 = int(input("Enter number of times you want to repeat the vowels: "))

vowel(userInput,userInput1)
