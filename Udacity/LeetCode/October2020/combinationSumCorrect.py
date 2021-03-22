class Solution:
    def combinationSum(self, candidates, target):
        candidates_length = len(candidates)
        for element in range(candidates_length):
            if target < min(candidates[element]):
                return []
        candidates_lst = []
        for value in range(candidates_length):
            if candidates[value] == target:
                candidates.append([target])
            else:
                for prev in self.combinationSum(candidates[value:], target - candidates[value]):
                    candidates_lst.append([candidates[value]] + prev)

        return candidates_lst

sol = Solution()
candidates = [2, 3, 6, 7]
target = 6
combinations = sol.combinationSum(candidates, target)
print("Combinations: ", combinations)