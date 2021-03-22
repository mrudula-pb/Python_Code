# Write a function that reverses a string. The input string is given as an array of characters char[].
# Do not allocate extra space for another array, you must do this by modifying the input array in-place
# with O(1) extra memory.
# You may assume all the characters consist of printable ascii characters.
#
# Example 1:
#
# Input: ["h","e","l","l","o"]
# Output: ["o","l","l","e","h"]
# Example 2:
#
# Input: ["H","a","n","n","a","h"]
# Output: ["h","a","n","n","a","H"]

class Solution:
    def reverseString(self, Input):
        # Approach 1
        # print(reversed(Input)) # prints list_reverseiterator object
        # for item in reversed(Input):
        #     print(item)

        # Approach 2
        # for item in Input[::-1]:
        #     print(item)

        # Approach 3
        length = int(len(Input)/2)
        i = 0
        for item in range(length):
            swap = Input[item]
            Input[item] = Input[-1-i]
            Input[-1-i] = swap
            i += 1
        return Input


solution = Solution()
Input = ["h","e","l","l","o"]
solution.reverseString(Input)
