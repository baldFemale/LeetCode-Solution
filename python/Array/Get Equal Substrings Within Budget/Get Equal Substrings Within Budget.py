class Solution(object):
    def equalSubstring(self, s, t, maxCost):
        """
        :type s: str
        :type t: str
        :type maxCost: int
        :rtype: int
        """
        A = [abs(ord(i) - ord(j)) for i, j in zip(s, t)]

        cost = maxCost

        res = 0
        i = 0

        for j in range(len(s)):
            cost -= A[j]

            while i < len(s) and cost < 0:
                cost += A[i]
                i += 1

            res = max(res, j - i + 1)

        return res
