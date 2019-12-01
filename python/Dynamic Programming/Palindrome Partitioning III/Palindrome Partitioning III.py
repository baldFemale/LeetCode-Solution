class Solution:
    def palindromePartition(self, s: str, k: int) -> int:

        def count(s):
            temp_s = s[::-1]
            c = 0
            for i in range(len(s) // 2):
                if s[i] != temp_s[i]:
                    c += 1
            return c

        cache = {}

        def dp(i, j):
            if (i, j) in cache:
                return cache[(i, j)]

            if i + 1 == j:
                cache[(i, j)] = 0
                return 0

            if j == 1:
                cache[(i, j)] = count(s[:i + 1])
                return cache[(i, j)]

            temp = 1000
            for cur in range(j - 1, i + 1):
                temp = min(temp, dp(cur - 1, j - 1) + count(s[cur:i + 1]))
            cache[(i, j)] = temp
            return temp

        return dp(len(s) - 1, k)
