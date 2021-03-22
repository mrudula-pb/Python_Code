# Given an array of integers nums and an integer k, return the number
# of unique k-diff pairs in the array.
#
# A k-diff pair is an integer pair (nums[i], nums[j]), where the following are true:
#
# 0 <= i, j < nums.length
# i != j
# a <= b
# b - a == k

import itertools

class Solution:
    # def sort_asec(self, nums):
    #     len_nums = len(nums)
    #     for first in range(0, len_nums):
    #         for second in range(first + 1, len_nums):
    #             if nums[first] > nums[second]:
    #                 temp = nums[first]
    #                 nums[first] = nums[second]
    #                 nums[second] = temp
    #     nums_sorted = nums
    #     return nums_sorted

    def findPairs(self, nums, k):
        len_nums = len(nums)
        for first in range(0, len_nums):
            for second in range(first + 1, len_nums):
                while nums[first] > nums[second]:
                    temp = nums[first]
                    nums[first] = nums[second]
                    nums[second] = temp
        print(nums)
        for value in zip(nums, nums[1:]):

             print(value)
        #pairs = set(tuple_pairs)
        #pairs = [t for t in (set(tuple(i) for i in tuple_pairs))]
        #print(pairs)
        #return len(pairs)



sol = Solution()
nums = [3,1,4,1,5]
target = 2
value = sol.findPairs(nums, target)
print(value)

---------------------------------------------
class Solution:
    def findPairs(self, nums, k):
        len_nums = len(nums)
        tuple_pairs = []
        for first in range(0, len_nums):
            for second in range(first + 1, len_nums):
                if nums[first] > nums[second]:
                    temp = nums[first]
                    nums[first] = nums[second]
                    nums[second] = temp
                    if nums[second] - nums[first] == k and nums[first] <= nums[second]:
                        tuple_pairs.append((nums[first], nums[second]))
        # tuple_pairs = [(nums[first], nums[second]) for first in range(len_nums)
        #              for second in range(first + 1, len_nums) if
        #             nums[second] - nums[first] == k and nums[first] <= nums[second]]
        pairs = set(tuple_pairs)
        return len(pairs)


sol = Solution()
nums = [3, 1, 4, 1, 5]
target = 2
# nums_sort_asec_list = sol.sort_asec(nums)
# print("Numbers in ascending order: ",nums_sort_asec_list)
# sol.findPairs(nums_sort_asec_list, target)

value = sol.findPairs(nums, target)
print(value)
