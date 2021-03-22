
#Part 4: Define a function to calculate the mean, median, and range (range = max-min) of a
# given list of numbers
# #hint: use the 'statistics' library for mean and median import statistics my_list = [1,3,5,4,2,6,8,4,8,9,11]

import statistics
class Solution:
    def calculate_MeanMedianRange(self, lst):
        # Mean
        total = 0
        for item in lst:
            total += item
        mean = int(total/2)
        #print("Mean is: " + str(mean))

        # Median in a sorted list
        new_lst = sorted(lst)
        lst_length = len(new_lst)
        median = new_lst[int(lst_length/2)]
        #print("Median is: " + str(median))

        # finding Max, Min value
        max = new_lst[lst_length-1]
        min = new_lst[0]
        range = max - min

        # Range, range = max-min
        #print("Range is: " + str(range))
        return mean, median, range

solution = Solution()
my_list = [1,3,5,4,2,6,8,4,8,9,11]
mean, median, range = solution.calculate_MeanMedianRange(my_list)

print("Mean is: " + str(mean))
print("Median is: " + str(median))
print("Range is: " + str(range))