
def add_one(arr):
    """
    :param: arr - list of digits representing some number x
    return a list with digits represengint (x + 1)
    """
    length_array = len(arr)
    print(arr)
    new_arr = []
    for value in arr[::-1]:
        #print(value)
        if value in range(0, 8):
            value += 1
            new_arr.append(value)
        print(new_arr)
    pass

add_one([1,2,3])