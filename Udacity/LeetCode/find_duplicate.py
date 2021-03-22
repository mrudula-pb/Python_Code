import collections


class Solution:
    def findDuplicates(self, nums):
        y=collections.Counter(nums)
        # [i for i in y if y[i] == 2]
        a = []
        for i in y:
            if y[i] == 2:
                a.append(i)
        print(a)


solution = Solution()
num_list = [2,3,2,3,4,5,6,4]

solution.findDuplicates(num_list)