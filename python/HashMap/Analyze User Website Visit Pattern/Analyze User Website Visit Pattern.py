from collections import defaultdict
from collections import Counter
from itertools import combinations


class Solution(object):
    def mostVisitedPattern(self, username, timestamp, website):
        """
        :type username: List[str]
        :type timestamp: List[int]
        :type website: List[str]
        :rtype: List[str]
        """
        d = defaultdict(list)

        for t, u, w in sorted(zip(timestamp, username, website)):
            d[u].append(w)

        c = Counter()
        for u in d:
            c += Counter(set(seq for seq in combinations(d[u], 3)))
        target = max(c.values())

        return min(list(k) for k in c if c[k] == target)
