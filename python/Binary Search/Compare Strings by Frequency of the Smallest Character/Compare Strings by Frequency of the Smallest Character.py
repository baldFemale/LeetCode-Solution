from collections import Counter
import bisect


class Solution(object):
    def numSmallerByFrequency(self, queries, words):
        """
        :type queries: List[str]
        :type words: List[str]
        :rtype: List[int]
        """
        w = []
        for word in words:
            c = Counter(word)
            k = sorted(c.keys())
            w.append(c[k[0]])
        w.sort()

        res = []
        for q in queries:
            c = Counter(q)
            k = sorted(c.keys())
            t = c[k[0]]
            index = bisect.bisect(w, t)
            res.append(len(w) - index)
        return res
