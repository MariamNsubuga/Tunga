'''
Write a program to replace 'yt' in 'Python' with the string entered by the user.
Create a string named language with the value "Python".
Take string as an input for ch variable.
Use the replace() method to replace "yt" with user-entered string stored in ch.
Print the new string.
Hint: Use the string replace() method. This method takes two arguments.
oldValue - a substring we want to replace
newValue - a substring that replaces the oldValue
Example Test Input ab Expected Output Pabhon
'''

language = "Python"
try:

    ch = input("Enter two characters: ")
    print("The text we want to replace is", language,"we want to replace (YT) with ",ch)
    if (len(ch) == 2):
        new_language=language.replace("y",ch[0])
        new_languages = new_language.replace("t",ch[1])
        print(new_languages)
    else:
        print("Characters should only be two.")
except ValueError:
    print("Inputs must be strings")