class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:

        self.length = len(nums)
        self.ans = []

        def backtrack(tmp):
            if len(tmp) == self.length:
                self.ans.append(list(tmp))

            for i in range(self.length):
                if visited[i]:
                    continue
                else:
                    tmp.append(nums[i])
                    visited[i] = True
                    backtrack(tmp)
                    tmp.pop()
                    visited[i] = False

        visited = [False] * self.length

        backtrack([])

        return self.ans
