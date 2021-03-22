from itertools import combinations

def numIdenticalPairs(nums):
    count = 0
    length = (len(nums))
    for i in range(length):
        for j in range(length):
            if nums[i] == nums[j] and i < j:
                count += 1
    return count


nums = [1,2,3]
value = numIdenticalPairs(nums)
print(value)