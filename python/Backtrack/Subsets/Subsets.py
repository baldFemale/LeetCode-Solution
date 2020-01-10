class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:

        self.length = len(nums)
        self.ans = []

        def backtrack(cur, tmp):

            self.ans.append(list(tmp))

            for i in range(cur, self.length):
                if visited[i]:
                    continue
                else:
                    visited[i] = True
                    tmp.append(nums[i])
                    backtrack(i + 1, tmp)
                    tmp.pop()
                    visited[i] = False

        visited = [False] * self.length
        backtrack(0, [])
        return self.ans

