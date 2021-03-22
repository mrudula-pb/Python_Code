from itertools import permutations


class Solution:
    def largestTimeFromDigits(a):
        best = -1
        for h1, h2, m1, m2 in permutations(a):
            hour = h1 * 10 + h2
            minute = m1 *10 + m2

            if 0 <= hour < 24 and 0 <= minute < 60:
                best = max(best, hour * 60 + minute)
        if best < 0:
            return ""

        best_hr, best_minute = divmod(best, 60)
        return f"{best_hr:02}:{best_minute:02}"

    largestTimeFromDigits([1,2,3,4])