class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:

        self.ans = []

        def backtrack(cur, tmp):
            if sum(tmp) == target:
                self.ans.append(list(tmp))
            elif sum(tmp) > target:
                pass
            else:
                for i in range(cur, len(candidates)):
                    tmp.append(candidates[i])
                    backtrack(i, tmp)
                    tmp.pop()

        backtrack(0, [])

        return self.ans