
def binary_search(array, target):
    '''Write a function that implements the binary search algorithm using iteration

    args:
      array: a sorted array of items of the same type
      target: the element you're searching for

    returns:
      int: the index of the target, if found, in the source
      -1: if the target is not found
    '''

    lower_bound = 0
    upper_bound = len(array)
    center_of_array = int(lower_bound + upper_bound/2)

    while lower_bound <= upper_bound:
    #for element in array[lower_bound:upper_bound + 1]:
        #print("Target: ", target)
        #print("Lower Bound: ", lower_bound)
        #print("Upper Bound: ", upper_bound)
        #print(center_of_array)
        if target == array[center_of_array]:
            return center_of_array
        elif target > array[center_of_array]:
            lower_bound = center_of_array + 1
            # input_list[input_list.index(element)] = None
            array[:center_of_array + 1] = [None for item in array[:center_of_array + 1]]
            center_of_array = int((lower_bound + upper_bound) / 2)
            #print(center_of_array)
        elif target < array[center_of_array]:
            upper_bound = center_of_array - 1
            array[center_of_array:] = [None for item in array[center_of_array:]]
            center_of_array = int((lower_bound + upper_bound) / 2)
        else:
            return -1

    return center_of_array

array = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
target = 6

index_of_target = binary_search(array, target)
print("Index of Target value: ", index_of_target)