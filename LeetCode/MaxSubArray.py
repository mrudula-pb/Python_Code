# Find Max Sub Array

def maxArray(nums):
    arraySum = 0
    result = 6
    lengthOfArray = len(nums)
    for sub_array in nums[lengthOfArray-1]:
        min_element = sub_array
        max_element = nums[:4]

        four_elements = max_element

        for n in four_elements:
            arraySum = arraySum + n
        print(arraySum)

        if arraySum == result:
            return arraySum


def main():
    my_array = [-2,1,-3,4,-1,2,1,-5,4]
    value = maxArray(my_array)
    print(value)


if __name__ == '__main__':
    main()
