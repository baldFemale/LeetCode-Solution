class Solution(object):
    def repeatedStringMatch(self, A, B):
        """
        :type A: str
        :type B: str
        :rtype: int
        """
        b = len(B)
        a = len(A)
        A = A * ((b // a + 1) * 2)

        mod = 10001

        p = 113
        cur = 0
        for i in B:
            cur += (ord(i) - ord("a")) * p
            p *= 113
        hb = cur % mod

        p = 113
        cur = 0
        for i in A[:b]:
            cur += (ord(i) - ord("a")) * p
            p *= 113
        ha = cur % mod

        if ha == hb and A[:b] == B:
            return b // a + 1 if b % a != 0 else b // a

        for j, i in enumerate(A[b:]):
            cur -= (ord(A[j % b]) - ord("a")) * 113
            cur /= 113
            cur += (ord(A[b + j]) - ord("a")) * p / 113
            ha = cur % mod
            if ha == hb and A[j + 1:j + b + 1] == B:
                return (j + b + 1) // a + 1 if (j + b + 1) % a != 0 else (j + b + 1) // a
        return -1
