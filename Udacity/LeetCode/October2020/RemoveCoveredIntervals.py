# Given a list of intervals, remove all intervals that are covered by another interval in the list.
# Interval [a,b) is covered by interval [c,d) if and only if c <= a and b <= d.
# After doing so, return the number of remaining intervals.
# Input: intervals = [[1,4],[3,6],[2,8]]
# Output: 2
# Explanation: Interval [3,6] is covered by [2,8], therefore it is removed.


class Solution:
    def removeCoveredIntervals(self, intervals) :
        integer = 0
        totalIntervals = len(intervals)
        for i in range(len(intervals)):
            for j in range(len(intervals)):
                if j != i:
                    if intervals[j][0] <= intervals[i][0] and intervals[j][1] >= intervals[i][1]:
                        totalIntervals -= 1
                        break
        return totalIntervals

sol = Solution()
intervals = [[1,4],[3,6],[2,8]]
value = sol.removeCoveredIntervals(intervals)
