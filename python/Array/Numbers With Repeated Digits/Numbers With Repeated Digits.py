class Solution(object):
    def numDupDigitsAtMostN(self, N):
        """
        :type N: int
        :rtype: int
        """

        def permutation(m, n):
            return 1 if n == 0 else permutation(m, n - 1) * (m - n + 1)

        res = 0

        n = str(N)
        res += sum(9 * permutation(9, i - 1) for i in range(1, len(n)))

        i = 0
        s = set()
        while i < len(n):
            for j in range(0 if i != 0 else 1, int(n[i])):
                if str(j) not in s:
                    res += permutation(9 - i, len(n) - i - 1)
            if n[i] in s:
                break
            s.add(n[i])
            i += 1

        return N - res - (i == len(n))
