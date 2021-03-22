# Given an array nums, write a function to move all 0's to the end of it while maintaining
# the relative order of the non-zero elements.
#
# Example:
#
# Input: [0,1,0,3,12]
# Output: [1,3,12,0,0]

class Solution:
    def moveZeroes(self, nums):
        """
        Do not return anything, modify nums in-place instead.
        """
        move_element = 0
        pos = 0
        length = len(nums)
        for i in range(length):
            if nums[i] != 0:
                nums[pos], nums[i] = nums[i], nums[pos]
                pos += 1
        return nums
solution = Solution()

nums = [0,1,0,3,12]
value = solution.moveZeroes(nums)
print(value)