class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:

        self.length = len(nums)
        self.ans = []

        def backtrack(tmp):
            if len(tmp) == self.length:
                print(tmp)
                self.ans.append(list(tmp))

            for i in range(self.length):
                if visited[i] or (i > 0 and nums[i] == nums[i - 1] and not visited[i - 1]):
                    continue
                else:
                    tmp.append(nums[i])
                    visited[i] = True
                    backtrack(tmp)
                    tmp.pop()
                    visited[i] = False

        visited = [False] * self.length

        nums.sort()
        backtrack([])

        return self.ans