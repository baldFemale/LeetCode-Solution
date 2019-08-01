class Solution(object):
    def minRefuelStops(self, target, startFuel, stations):
        """
        :type target: int
        :type startFuel: int
        :type stations: List[List[int]]
        :rtype: int
        """
        dp = [0 for i in range(len(stations))]

        dp = [startFuel] + dp

        for i in range(len(stations)):
            for j in range(i, -1, -1):
                if stations[i][0] <= dp[j]:
                    dp[j + 1] = max(dp[j + 1], dp[j] + stations[i][1])
        for i in range(len(dp)):
            if dp[i] >= target:
                return i
        return -1
