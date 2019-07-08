class Solution(object):
    def mincostTickets(self, days, costs):
        """
        :type days: List[int]
        :type costs: List[int]
        :rtype: int
        """
        dp = [float("inf") for day in range(366)]
        dp[0] = 0

        days = set(days)

        for day in range(1, 366):
            if day not in days:
                dp[day] = dp[day - 1]
            else:
                dp[day] = min(dp[day], dp[day - 1] + costs[0])
                dp[day] = min(dp[day], dp[max(0, day - 7)] + costs[1])
                dp[day] = min(dp[day], dp[max(0, day - 30)] + costs[2])
        return dp[-1]