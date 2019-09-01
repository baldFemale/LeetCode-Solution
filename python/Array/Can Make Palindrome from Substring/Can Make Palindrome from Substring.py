class Solution(object):
    def canMakePaliQueries(self, s, queries):
        """
        :type s: str
        :type queries: List[List[int]]
        :rtype: List[bool]
        """
        counters = []
        temp = [0 for i in range(26)]
        counters.append(list(temp))
        for i in range(len(s)):
            temp[ord(s[i]) - ord("a")] += 1
            counters.append(list(temp))
        res = []
        for q in queries:
            t = [counters[q[1] + 1][i] - counters[q[0]][i] for i in range(26)]
            t = [i % 2 for i in t]
            if (q[1] - q[0] + 1) % 2 == 0:
                res.append(sum(t) // 2 <= q[2])
            else:
                res.append((sum(t) - 1) // 2 <= q[2])
        return res
