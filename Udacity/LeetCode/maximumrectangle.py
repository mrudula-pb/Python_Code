class Solution:
    def maximalRectangle(self, A):
        length_A, B, b, array_1, array_2 = len(A), 0, 0, [], []
        if length_A == 0: return 0
        n = len(A[0])
        for i in range(length_A):
            if A[i][0] == "0":
                A[i][0] = b = 0
            else:
                A[i][0], b, B = 1, b + 1, max(B, b + 1)
        for j in range(1, n):
            for i in range(length_A):
                if A[i][j] == "0":
                    A[i][j] = 0
                    if len(array_2) > 0: array_1, array_2 = array_1 + [array_2], []
                else:
                    A[i][j], array_2 = A[i][j - 1] + 1, array_2 + [A[i][j - 1] + 1]
            if len(array_2) > 0: array_1, array_2 = array_1 + [array_2], []
        for array_2 in array_1:
            for i in range(1, len(array_2) + 1):
                for j in range(len(array_2) + 1 - i):
                    B = max(B, min(array_2[j:j + i]) * i)
        return B

sol = Solution()

value = sol.maximalRectangle(
    [["1", "0", "1", "0", "0"],
     ["1", "0", "1", "1", "1"],
     ["1", "1", "1", "1", "1"],
     ["1", "0", "0", "1", "0"]])
print(value)
