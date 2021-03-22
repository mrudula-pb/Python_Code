
class add_one:
    def add_one(self, arr):
        if arr == [9]:
            return [1, 0]
        if arr[-1] < 9:
            arr[-1] += 1
        else:
            arr = add_one(arr[:-1]) + [0]
        return arr

arr = [9, 0, 9]
solution = [9, 1, 0]

output = add_one(arr)

for index, element in enumerate(output):
    if element != solution[index]:
        print("Fail")
    print("Pass")