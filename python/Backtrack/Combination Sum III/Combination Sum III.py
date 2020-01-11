class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:

        self.ans = []

        def backtrack(tmp, cur):
            if len(tmp) == k and sum(tmp) == n:
                self.ans.append(list(tmp))
            elif len(tmp) < k and sum(tmp) < n:
                for i in range(cur, 10):
                    tmp.append(i)
                    backtrack(tmp, i + 1)
                    tmp.pop()

        backtrack([], 1)
        return self.ans
