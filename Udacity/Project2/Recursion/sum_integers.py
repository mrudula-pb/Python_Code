
class Solution:
    def sum_integers(self, number):
        if number == 1:
            return 1
        return number + self.sum_integers(number - 1)

solution = Solution()
value = solution.sum_integers(3)
print("Sum of Integers: " + str(value))