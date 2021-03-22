class Solution:
    def removeElement(self, nums, val):
        nums.sort()
        length = 0
        for num in nums:
            if num != val:
                nums[length] = num
                length += 1
        return length

solution = Solution()
nums = [3,2,2,3,1,4,4]
value = 3
element = solution.removeElement(nums, value)
print(element)