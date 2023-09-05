'''
Given a string, find and return the index of the first character that is not repeated.
Example Test Input: python.program.py Expected Output: 3
'''
title="Given a string, find and return the index of the first character that is not repeated."
r=len(title)

print(title.center(r+3,'*'))
def check_repeated_words(string):
    
    index = -1
    fnc = ""
    if len(string) == 0 :
        print("EMTPY STRING")
    
    for i in string:
        if string.count(i) == 1:
            fnc += i
            break
        else:
            index += 1
    if index == len(string)-1 :
        print("All characters are repeating ")
    else:
        print("First non-repeating character is", fnc, "at position",string.rfind(fnc))
word = input("Enter combination of words to be tested: ")
check_repeated_words(word)
