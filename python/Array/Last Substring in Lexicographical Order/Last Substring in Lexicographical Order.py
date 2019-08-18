from collections import defaultdict


class Solution(object):
    def lastSubstring(self, s):
        """
        :type s: str
        :rtype: str
        """
        n = len(s)
        d = defaultdict(list)
        for i, j in enumerate(s):
            d[j].append(i)
        if len(d) == 1:
            return s
        m = max(d.keys())
        start = d[m]

        c = 0
        while len(start) > 1:
            c += 1
            start = [i + 1 for i in start if i + 1 <= n - 1]
            m = max([s[i] for i in start])
            start = [i for i in start if s[i] == m]
        return s[start[0] - c:]
