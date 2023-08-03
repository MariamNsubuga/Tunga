'''
Write a program to create a new list from an existing list using list slicing.
Create a list named my_list with items 'p','y','t','h','o','n'.
Use the slicing notation to get a new list from the second to the second-last items from my_list.
Print the new list.
'''

my_list = ['p','y','t','h','o','n']
print("This is the full list", my_list)
new_my_list = my_list[1:-1]

print("This is a sliced list",new_my_list)