# You have been given an array containg numbers. Find and return the largest sum in a contiguous subarray within the input array.

def max_sum_subarray(arr):
    i = 0
    j = 0
    sum_current = 0
    sum_previous = 0
    array_length = len(arr)

    for value_outer_loop in arr[j:]:
        print(value_outer_loop)
        if j == array_length:
            array_length-i
        for value_inner_loop in arr[j:array_length]:
            print(value_inner_loop)
            print(array_length)
            sum_current += value_inner_loop
        print(sum_current)
        i += 1
        j += 1
        if sum_current >= sum_previous:
            sum_previous = sum_current
            sum_current = 0
        else:
            sum_current = 0


    return sum_previous


sum = max_sum_subarray([-12, 15, -13, 14, -1, 2, 1, -5, 4])
print(sum)