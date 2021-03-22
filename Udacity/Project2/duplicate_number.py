def duplicate_number(arr):
    """
    :param - array containing numbers in the range [0, len(arr) - 2]
    return - the number that is duplicate in the arr
    """
    array_length = len(arr)
    #print(array_length)
    i = 0
    j = 1
    for first in arr[i:]:
        for second in arr[j:]:
            if first == second:
                return first
        j += 1

Test_1 = duplicate_number([0, 2, 3, 1, 4, 5, 3])
print(Test_1)

Test_2 = duplicate_number([0, 1, 5, 4, 3, 2, 0])
print(Test_2)

Test_3 = duplicate_number([0, 1, 5, 5, 3, 2, 4])
print(Test_3)