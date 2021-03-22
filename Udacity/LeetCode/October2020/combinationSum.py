class Solution:
    def combinationSum(self, candidates, target):
        print(candidates)
        candidates_lst = []
        candidates_length = len(candidates)
        candidates_indexes = len(candidates)
        for first in range(0, candidates_length):
            for second in range(first + 1, candidates_length):
                if (candidates[first]) < target:
                    sum = candidates[first] + candidates[first]
                    while sum < target:
                        sum += candidates[first]
                    if sum == target:
                        candidates_lst.append(candidates[first])
                elif candidates[first] == target:
                    candidates_lst.append(candidates[first])
                #continue

                if (candidates[first] and candidates[second]) < target:
                    sum = candidates[first] + candidates[second]
                    if sum < target:
                        continue
                    if sum == target:
                        candidates_lst.append(candidates[first])

        return candidates_lst

sol = Solution()
candidates = [2, 3, 6, 7]
target = 6
combinations = sol.combinationSum(candidates, target)
print("Combinations: ", combinations)