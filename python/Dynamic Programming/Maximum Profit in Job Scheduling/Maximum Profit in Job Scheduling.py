import bisect


class Solution(object):
    def jobScheduling(self, startTime, endTime, profit):
        """
        :type startTime: List[int]
        :type endTime: List[int]
        :type profit: List[int]
        :rtype: int
        """

        jobs = [(startTime[i], endTime[i], profit[i]) for i in range(len(profit))]
        jobs.sort(key=lambda x: x[0])
        starts = [i[0] for i in jobs]
        print(jobs)
        cache = {}

        def dp(x):
            if x in cache:
                return cache[x]

            else:
                if x >= len(profit):
                    cache[x] = 0
                    return 0

                else:
                    s, e, p = jobs[x]
                    index = bisect.bisect_left(starts, e)
                    p += dp(index)
                    cache[x] = max(p, dp(x + 1))

                    return cache[x]

        return dp(0)
