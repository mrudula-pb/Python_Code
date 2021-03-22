
# Asterisks for unpacking into function call

fruits = ['lemon', 'pear', 'watermelon', 'tomato']
print(fruits[0], fruits[1], fruits[2], fruits[3])

# Using asterisks
print(*fruits)
# --------------------------------------

#
def transpose_list(list_of_lists):
    return [
        list(row)
        for row in zip(*list_of_lists)
    ]
print(transpose_list([[1, 4, 7], [2, 5, 8], [3, 6, 9]]))
#[[1, 2, 3], [4, 5, 6], [7, 8, 9]])

# Using * multiple times
fruits =['lemon', 'pear', 'watermelon', 'tomato']
numbers = [2,1,3,4,7]
print(*fruits, *numbers)

# Using ** numtiple times
date_info = {'year': "2020", 'month': "01", 'day': "01"}
track_info = {'artist': "Beethoven", 'title': 'Symphony No 5'}
filename = "{year}-{month}-{day}-{artist}-{title}.txt".format(**date_info,**track_info)
print(filename)

# date_info = {'year': "2020", 'month': "01", 'day': "01"}
# track_info = {'artist': "Beethoven", 'title': 'Symphony No 5'}
# filename = "{year}-{month}-{day}-{artist}-{title}.txt".format(**date_info, **track_info,)
# print(filename)

from random import randint

def roll(*dice):
    return sum(randint(1, die) for die in dice)

value = roll(6,6)
print(value)

arr = ['sunday', 'monday', 'tuesday', 'wednesday']

# without using asterisk
print(' '.join(map(str,arr)))

# using asterisk
print (*arr)



