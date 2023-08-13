'''
create a function that prints our dictionary in the way its show in the image
'''

picnicItems = {'sandwiches': 4, 'apples': 12, 'cups': 4, 'cookies': 8000}


def tables():
    title = "PINIC ITEMS"
    x = title.center(20, "-")
    print(x)

    for key, value in picnicItems.items():
        print(key, '\t', "----", '\t', value, '\n')


tables()
