'''
 Write a program to check if the first and last characters of a string are equal.
Take string as input and assign it to check variable.
Use list indexing to check if the first and the last character of a string are equal or not. use( list() to convert
a string to list)
If yes, print Equal. Else print Not Equal.
'''
print("This program to check if the first and last characters of a string are equal.")
print("----------------------------------------------------------------------------------------------")
st = input("Enter a word you want to compare: ")
while (str.isalpha(st)):
    try:
        if (st[0] == st[-1]):
            print("The first and last characters of a string are equal.")
            break
        else:
            print("The first and last characters of a string are not equal.")
            break
    except ValueError:
        print("Inputs should only be integres")

else:
  print("Input must be strings only") 
    