# Given an array nums of n integers, are there elements a, b, c in nums
# such that a + b + c = 0? Find all unique triplets in the array which gives the sum of zero.
#
# Notice that the solution set must not contain duplicate triplets.
#
#
#
# Example 1:
#
# Input: nums = [-1,0,1,2,-1,-4]
# Output: [[-1,-1,2],[-1,0,1]]

# class Solution:
#     def threeSum(self, nums):
#         len_nums = len(nums)
#         for first in range(0, len_nums):
#             for second in range(first + 1, len_nums):
#                 if nums[first] > nums[second]:
#                     temp = nums[first]
#                     nums[first] = nums[second]
#                     nums[second] = temp
#         print(nums)
#         max_num = nums[len_nums]
#         min_num = nums[0]

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:

        nums.sort()
        res = []

        for i in range(len(nums) - 2):  # 1
            if i > 0 and nums[i] == nums[i - 1]:  # 2
                continue
            left = i + 1  # 3
            right = len(nums) - 1  # 4

            while left < right:
                temp = nums[i] + nums[left] + nums[right]

                if temp > 0:
                    right -= 1

                elif temp < 0:
                    left += 1

                else:
                    res.append([nums[i], nums[left], nums[right]])  # 5
                    while left < right and nums[left] == nums[left + 1]:  # 6
                        left += 1
                    while left < right and nums[right] == nums[right - 1]:  # 7
                        right -= 1  # 8

                    right -= 1  # 9
                    left += 1  # 10


solution = Solution()
nums = [-1,0,1,2,-1,-4]
sort_nums = solution.threeSum(nums)
print(sort_nums)

