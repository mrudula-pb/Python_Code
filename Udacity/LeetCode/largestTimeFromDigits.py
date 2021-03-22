# Given an array of 4 digits, return the largest 24 hour time that can be made.
#
# The smallest 24 hour time is 00:00, and the largest is 23:59.  Starting from 00:00, a time is larger if more time has elapsed since midnight.
#
# Return the answer as a string of length 5.  If no valid time can be made, return an empty string.
from itertools import combinations

class Solution:
    def largestTimeFromDigits(a):
        beg = 0
        end = 5
        count = 0
        string_list = []
        length_a = len(a)
        if length_a == 4:
            for number in a:
                if number >= 0 and number <= 5:
                    count += 1
            print(count)
            if count == 3:
                print(list(combinations(a, 2)))

    A = [1,2,3,9]
    value = largestTimeFromDigits(A)
    print(value)