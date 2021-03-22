# Given a sorted array that may have duplicate values, use binary search to find the first and last indexes of a given value.
#
# For example, if you have the array [0, 1, 2, 2, 3, 3, 3, 4, 5, 6] and the given value is 3, the answer will be [4, 6] (because the value 3 occurs first at index 4 and last at index 6 in the array).
#
# The expected complexity of the problem is  𝑂(𝑙𝑜𝑔(𝑛)) .
#

def binary_search(target, source):
    if len(source) == 0:
        return print("Array size is 0")
    arr_length = len(source)
    center = (arr_length - 1) // 2
    if source[center] == target:
        return center
    elif source[center] < target:
        return binary_search(target, source[center+1:])
    else:
        return binary_search(target, source[:center])


def find_first_index(arr, number):
    index = binary_search(number, arr)
    firstIndex = index
    #if not index:
        #return print("Element ", index ,"not present in arr")
    while arr[index] == target:
        if index == 0:
            return index
        elif arr[index - 1] == target:
            index -= 1
            firstIndex = index
        else:
            return firstIndex

def find_last_index(arr, number):
    index = binary_search(number, arr)
    lastIndex = index
    if not index:
        return print("Element ", index, "not present in arr")
    while arr[index] == target:
        if index == 0:
            return index
        elif arr[index + 1] == target:
            index += 1
            lastIndex = index
        else:
            return lastIndex

target = 2
arr = [0, 1, 2, 2, 3, 3, 3, 4, 5, 6]
print("First index of ", target, ":", find_first_index(arr, target))
print("Last index of ", target, ":", find_last_index(arr, target))