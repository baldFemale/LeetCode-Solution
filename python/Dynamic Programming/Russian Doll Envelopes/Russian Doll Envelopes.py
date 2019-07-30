import bisect


class Solution(object):
    def maxEnvelopes(self, envelopes):
        """
        :type envelopes: List[List[int]]
        :rtype: int
        """
        if not envelopes:
            return 0

        envelopes.sort(key=lambda x: (x[0], -x[1]))

        temp = [i[1] for i in envelopes]

        dp = []
        res = 0
        for i in temp:
            index = bisect.bisect_left(dp, i)
            if index == len(dp):
                dp.append(i)
                res = max(res, len(dp))
            else:
                dp[index] = i
        return res
