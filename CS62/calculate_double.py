
#Part 2: Iterate through the given list, calculate each item's doubled value,
# then print out the results#hint: use a for loop my_list = [1,3,5,4,2,6,8,4,8,9,11]

class Solution:
    def calculate_double(self, int_list):
        double_list = []
        for item in int_list:
            double_item = item * item
            print(double_item)
            double_list.append(double_item)
        print(double_list)

solution = Solution()
int_list = [1,3,5,4,2,6,8,4,8,9,11]
solution.calculate_double(int_list)