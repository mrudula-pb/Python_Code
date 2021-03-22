
# using slicing
class Solution:
    def sum_array(self, a):
        if len(a) == 1:
            return a[0]
        return a[0] + self.sum_array(a[1:])

solution = Solution()
array =  [1, 2, 3, 4]
value = solution.sum_array(array)
print("Sum of array: " + str(value))