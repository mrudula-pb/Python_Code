
# iterative solution
class Solution:
    def sum_array_iter(self, array):
        result = 0
        for index in range(len(array)):
            result += array[index]
        return result

solution = Solution()
array = [5,5,5,5]
value = solution.sum_array_iter(array)
print("Sum of array: " + str(value))