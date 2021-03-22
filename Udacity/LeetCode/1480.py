# Given an array nums. We define a running sum of an array as runningSum[i] = sum(nums[0]…nums[i]).
#
# Return the running sum of nums.

class Solution:
    def runningSum(self, nums):
        runningSums = []
        i = 0
        sum = 0
        for value in nums:
            sum += value
            runningSums.append(sum)
            i += 1
        return runningSums


solution = Solution()
nums = [1,2,3,4]
value = solution.runningSum(nums)

nums_new = []
for n in value:
    nums_new.append(n)
print(nums_new)
