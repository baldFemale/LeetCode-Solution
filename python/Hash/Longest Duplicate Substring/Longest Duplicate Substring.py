from collections import defaultdict

prime = 10 ** 9 + 7
base = 26


class Solution(object):
    def longestDupSubstring(self, S):
        """
        :type S: str
        :rtype: str
        """

        def helper(s, n):
            max_base = pow(base, n - 1, prime)
            cur = 0
            for i in s[:n]:
                cur = (cur * base + ord(i)) % prime
            dic = defaultdict(list)
            dic[cur].append(n - 1)

            for j, i in enumerate(s[n:]):
                cur -= ord(s[j]) * max_base
                cur = (cur * base + ord(i)) % prime
                if cur in dic:
                    st = s[j + 1:j + n + 1]
                    for v in dic[cur]:
                        if st == s[v - n + 1:v + 1]:
                            return st
                dic[cur].append(j + n)
            return ""

        low = 0
        high = len(S)

        res = ""
        while low + 1 < high:
            mid = (low + high) // 2
            v = helper(S, mid)
            if v:
                res = v
                low = mid
            else:
                high = mid
        return res
