# Given an integer (signed 32 bits), write a function to check whether it is a power of 4.

class Solution:
    def isPowerOfFour(self, num: int) -> bool:
        i = 1
        while i < num:
            i *= 4

        return i == num


obj = Solution()
value = obj.isPowerOfFour()
print(value)