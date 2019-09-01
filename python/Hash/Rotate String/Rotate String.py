class Solution(object):
    def rotateString(self, A, B):
        """
        :type A: str
        :type B: str
        :rtype: bool
        """
        mod = 101

        p = 113
        cur = 0
        for i in B:
            cur += (ord(i) - ord("a")) * p
            p *= 113
        hb = cur % mod

        p = 113
        cur = 0
        for i in A:
            cur += (ord(i) - ord("a")) * p
            p *= 113
        ha = cur % mod

        if ha == hb and A == B:
            return True

        for j, i in enumerate(A):
            cur -= (ord(i) - ord("a")) * 113
            cur /= 113
            cur += (ord(i) - ord("a")) * p / 113
            ha = cur % mod
            if ha == hb and A[j + 1:] + A[:j + 1] == B:
                return True
        return False
