def binary_search_recursive_soln(array, target, start_index, end_index):
    if start_index > end_index:
        return -1

    mid_index = (start_index + end_index) // 2
    mid_element = array[mid_index]

    if mid_element == target:
        return mid_index
    elif target < mid_element:
        return binary_search_recursive_soln(array, target, start_index, mid_index - 1)
    else:
        return binary_search_recursive_soln(array, target, mid_index + 1, end_index)


array = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
target = 8
start_index = 0
end_index = len(array)-1

index_of_target = binary_search_recursive_soln(array, target, start_index, end_index)
print("Index of Target value: ", index_of_target)


def binary_search_recursive_soln(array, target, lower_bound, upper_bound):
    center_of_array = int((lower_bound + upper_bound) / 2)
    # print(center_of_array)

    if target == array[center_of_array]:
        return center_of_array
    return center_of_array
    if target > array[center_of_array]:
        lower_bound = center_of_array + 1
        array[:center_of_array + 1] = [None for item in array[:center_of_array + 1]]
        binary_search_recursive_soln(array, target, lower_bound, upper_bound)
    elif target < array[center_of_array]:
        upper_bound = center_of_array - 1
        array[center_of_array:] = [None for item in array[center_of_array:]]
        binary_search_recursive_soln(array, target, lower_bound, upper_bound)
    else:
        return -1


array = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
target = 8
start_index = 0
end_index = len(array) - 1

index_of_target = binary_search_recursive_soln(array, target, start_index, end_index)
print("Index of Target value: ", index_of_target)