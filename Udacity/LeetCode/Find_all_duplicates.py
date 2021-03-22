# Given an array of integers, 1 ≤ a[i] ≤ n (n = size of array), some elements appear twice and others appear once.
#
# Find all the elements that appear twice in this array.
#
# Could you do it without extra space and in O(n) runtime?

class Solution:


    def add(self, nums, numbers_dict):
        i = 0
        for value in nums:
            numbers_dict[i] = value
            i += 1
        return numbers_dict

    def findDuplicates(self, nums):
        count_list = []
        for value in nums:
            count = nums.count(value)
            if count == 2 and value not in count_list:
                count_list.append(value)
        print(count_list)

solution = Solution()
num_list = [4,3,2,7,8,2,3,1]

solution.findDuplicates(num_list)

# print(find_dup)
# numbers_dict = {}
# dict = solution.add(num_list, numbers_dict)

# for k, v in dict.items():
   # print(k, v)