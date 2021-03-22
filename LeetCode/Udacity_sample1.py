my_list = [0, 1, 2, 3, 4, 5]

# Print each value in my_list. Note you can use the "in" keyword to iterate over a list.
for value in my_list:
    print("Value in my_list: ", str(value))

# Print each index and value pair.
# print("Index and Value pair: ", list(enumerate(my_list)))

for index, value in enumerate(my_list):
    print("Index and Value pair: ", str(index), str(value))

# Print each number from 0 to 9 using a while loop.
i = 0
while (i < 10):
    print("Print number: ", i)
    i += 1

# Print each key and dictionary value. Note that you can use the "in" keyword
# to iterate over dictionary keys.
my_dict = {'a': 'jill', 'b': 'tom', 'c': 'tim'}
for key, value in my_dict.items():
    print(key, value)