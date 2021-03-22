# Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
#
# You may assume that each input would have exactly one solution, and you may not use the same element twice.
#
# You can return the answer in any order.

class Solution:
    # Using 2 for loops
    # def twoSum(self, nums, target):
    #     print(nums)
    #     output = []
    #     nums_length = len(nums)
    #     for first in range(nums_length):
    #         for second in range(first + 1, nums_length):
    #             if (nums[first] + nums[second]) == target:
    #                 output.append(first)
    #                 output.append(second)
    #             continue
    #     return output

    # Using dictionary
    def twoSum(self, nums, target):
        output = {}
        nums_length = len(nums)
        for id,value in enumerate(nums):
            if (target - value) in output:
                return output[target - value], id
            output[value] = id
        return -1



solution = Solution()
nums = [2,7,11,15,5,4]
target = 9
twoSum = solution.twoSum(nums, target)
print(twoSum)