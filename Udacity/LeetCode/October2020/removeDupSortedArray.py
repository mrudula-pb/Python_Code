# Given a sorted array nums, remove the duplicates in-place such that each element appears only once and returns the new length.
#
# Do not allocate extra space for another array, you must do this by modifying the input array in-place with O(1) extra memory.

# Example 1:
#
# Given nums = [1,1,2],
#
# Your function should return length = 2, with the first two elements of nums being 1 and 2 respectively.
#
# It doesn't matter what you leave beyond the returned length.

class Solution:
    def removeDuplicates(self, nums):
        temp = None
        length = 0
        for num in nums:
            if num != temp: #0,0=doesn't go to loop, 1, 1=doesn't go to loop
                nums[length] = num # num value i.e 0, 1
                temp = num #0, 1
                length += 1 # 1,2
        return length
solution = Solution()
nums = [0,0,1,1]
value = solution.removeDuplicates(nums)
print(value)