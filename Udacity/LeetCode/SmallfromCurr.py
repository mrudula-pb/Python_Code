
# Strategy: First sort numbers and then check the smallest numbers than current number

def smallerNumbersThanCurrent(nums_sort_dsec_list):
    nums_len = len(nums_sort_dsec_list)
    indexes = nums_len - 1
    for index in range(0, nums_len):
        value = indexes - index
        print("Smaller Numbers Than", nums_sort_dsec_list[index], ":", value)

def sort_asec(nums):
    len_nums = len(nums)
    for first in range(0, len_nums):
        for second in range(first + 1, len_nums):
            if nums[first] > nums[second]:
                temp = nums[first]
                nums[first] = nums[second]
                nums[second] = temp

    return nums

def sort_desc(nums):
    len_nums = len(nums)
    for first in range(0, len_nums):
        for second in range(first + 1, len_nums):
            if nums[first] < nums[second]:
                temp = nums[first]
                nums[first] = nums[second]
                nums[second] = temp
    return nums

nums = [8, 1, 2, 2, 3]
nums_sort_asec_list = sort_asec(nums)
print("Numbers in ascending order: ",nums_sort_asec_list)
nums_sort_dsec_list = sort_desc(nums)
print("Numbers in Descending order: ", nums_sort_dsec_list)

smallerNumbersThanCurrent(nums_sort_dsec_list)