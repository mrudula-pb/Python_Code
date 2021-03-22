def add_one(arr):
    """
    :param: arr - list of digits representing some number x
    return a list with digits represengint (x + 1)
    """
    indices = len(arr) - 1
    print("List: ", arr)
    print("No of elements in List: ", indices) #[0], [1], [2]

    new_arr = []
    carry = 0
    i = 0
    # new_list = list(arr[::-1])
    # print("Reversed list: ", new_list)
    # print(arr.index(arr[indices]))

    while indices >= 0:
        print("Value in arr: ", arr[indices])
        if arr[indices] in range(0, 9):
            #print(arr.index(arr[indices]))
            #print(len(arr) - 1)
            if arr.index(arr[indices]) == len(arr) - 1:
                arr[indices] += 1
                new_arr.insert(i, arr[indices])
                #print(new_arr)
                i += 1
            else:
                if carry == 1:
                    arr[indices] = carry + arr[indices]
                    if arr[indices] == 10:
                        add_zero = 0
                        new_arr.insert(i, add_zero)
                        #print(new_arr)
                        i += 1
                        carry = 1
                new_arr.insert(i, arr[indices])
                #print(new_arr)
                i += 1
                carry = 0
        elif arr[indices] == 9:
            #print(arr[indices])
            #print(arr.index(arr[indices]))
            #print(len(arr) - 1)
            if indices == len(arr) - 1:
                arr[indices] += 1
                if arr[indices] == 10:
                    add_zero = 0
                    new_arr.insert(i, add_zero)
                    #print(new_arr)
                    i += 1
                    carry = 1
            else:
                if carry == 1:
                    arr[indices] = carry + arr[indices]
                    if arr[indices] == 10:
                        add_zero = 0
                        new_arr.insert(i, add_zero)
                        i += 1
                        carry = 1
                        if indices == 0:
                            new_arr.insert(i, carry)
                    else:
                        new_arr.insert(i, arr[indices])
                        i += 1
                        carry = 0
        indices -= 1
    print(new_arr[::-1])

add_one([9, 9, 9])