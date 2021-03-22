
# using indexing
class Solution:
    def sum_array_index(self, array):
        index=0
        if len(array) == 1:
            return array[index]
        else:
            return array[index] + self.sum_array_index(array[index+1:])

solution = Solution()
array = [1,2,3,4]
value = solution.sum_array_index(array)
print("Sum of array: " + str(value))