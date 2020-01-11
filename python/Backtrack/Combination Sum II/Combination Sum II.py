class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:

        self.ans = []

        def backtrack(tmp, cur):

            if sum(tmp) == target:
                self.ans.append(list(tmp))
            elif sum(tmp) > target:
                pass
            else:
                for i in range(cur, len(candidates)):
                    if visited[i] or (i > 0 and candidates[i - 1] == candidates[i] and not visited[i - 1]):
                        continue
                    else:
                        tmp.append(candidates[i])
                        visited[i] = True
                        backtrack(tmp, i + 1)
                        tmp.pop()
                        visited[i] = False

        candidates.sort()
        visited = [False] * len(candidates)
        backtrack([], 0)

        return self.ans

