class Solution:
    def findComplement(self, num):
        place = 0
        complement = 0
        while num > 0:
            remainder = num % 2
            if remainder == 0:
                complement += 2 ** place
            place += 1
            num = num // 2
        return complement

sol = Solution()
value = sol.findComplement(101)
print(value)