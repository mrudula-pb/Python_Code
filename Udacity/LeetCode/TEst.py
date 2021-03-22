
class Solution:
    def containsNearbyAlmostDuplicate(nums, k, t):
        print(nums)
        length_lst = len(nums)
        print("Length of List: ", length_lst)
        print('K: ', k)
        print("T: ", t)
        if length_lst > k and nums[0] != 0:
            for i in range(0,len(nums)):
                add = i + k
                for j in range(add,len(nums)):
                    if abs(nums[i] - nums[j]) <= t:
                        # print(i , ',', j, "indices has duplicate value of" , nums[i])
                        if abs(i-j) <= k:
                            return True
                        return False
                    else:
                        continue
        else:
            return False

    nums = [1,2]
    k = 0
    t = 1
    value = containsNearbyAlmostDuplicate(nums, k, t)
    print(value)