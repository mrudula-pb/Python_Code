
class Solution:
    def containsNearbyAlmostDuplicate(nums, k, t):
        #print(nums)
        if t == 0:
            '''Checking for Duplicates in list'''
            for i in range(0,len(nums)):
                for j in range(1,len(nums)):
                    if nums[i] == nums[j]:
                        print(i , ',', j, "indices has duplicate value of" , nums[i])
                        if abs(i-j) <= k:
                            return True
                        return False
                    else:
                        continue
        else:
            for i in range(0,len(nums)):
                for j in range(1,len(nums)):
                    if abs(nums[i] - nums[j]) <= t:
                        if abs(i-j) <= k:
                            return True
                        return False
                    else:
                        return False

    nums = [1,3,1]
    k = 2
    t = 1
    value = containsNearbyAlmostDuplicate(nums, k, t)
    print(value)