
# Part 1: Take in user input for both heigh and eidth print out the area
## hint: Use the "input" function and don't forget to convert them to ints

class Solution:
    def print_area(self):
        height = input("Enter Height: ")
        width = input("Enter Width: ")

        area = (int(height) * int(width))
        print("Area is: " + str(area))

solution = Solution()
solution.print_area()