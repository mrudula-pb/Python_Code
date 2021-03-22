#
# test_dict = {'gfg' : [1, 3, 4], 'is' : [7, 6], 'best' : [4, 5]}
#
# # print original Dictionary
# print(test_dict)
#
# length = len(test_dict)
# print(length)
#
# for key, value in test_dict.items():
#     print(key, value)
#
# lst_keys = []
# lst_keys = test_dict.keys()
# print(lst_keys)
#
# lst_values = []
# lst_values = test_dict.values()
# print(lst_values)
#
# # Convert Key-Value list Dictionary to Lists of List
# # Using loop + items()
# lst = []
# for key, value in (test_dict.items()):
#     lst.append([key]+ value)
# print(lst)
#
# lst_1 = [[key] + value for key, value in test_dict.items()]
#
# print(lst_1)

# List Comprehensions
squares = []
for value in range(10):
    squares.append(value ** 2)
print(squares)

squares = list(map(lambda x:x ** 2, range(10))) #lambda variable: expression
print(squares)

squares = [x ** 2 for x in range(10)]
print(squares)

# this listcomp combines the elements of two lists
# if they are not equal:

# Convert Lists of List to Dictionary
test_list = [['a', 'b', 1, 2], ['c', 'd', 3, 4], ['e', 'f', 5, 6]]
print(test_list)

result = dict()
for sub in test_list:
    result[tuple(sub[:2])] = tuple(sub[2:])
print(result)

result = {tuple(sub[:2]):tuple(sub[2:]) for sub in test_list}
print(result)

# Python3 code to demonstrate working of
# Convert Key-Value list Dictionary to Lists of List
# Using loop + items()
test_dict = {'gfg' : [1, 3, 4], 'is' : [7, 6], 'best' : [4, 5]}

list_items = []
for key, value in test_dict.items():
    list_items.append([key] + value)
print(list_items)
