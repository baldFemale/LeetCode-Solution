class Solution(object):
    def canCross(self, stones):
        """
        :type stones: List[int]
        :rtype: bool
        """
        dic = {stones[i]: i for i in range(len(stones))}
        cache = {}

        def dp(i, k):
            if i == len(stones) - 1:
                cache[(i, k)] = True
                return True
            if (i, k) in cache:
                return cache[(i, k)]
            temp = False
            if stones[i] + k in dic and (stones[i] + k, k) not in cache:
                temp |= dp(dic[stones[i] + k], k)
            if stones[i] + k - 1 in dic and (stones[i] + k - 1, k - 1) not in cache and k - 1 != 0:
                temp |= dp(dic[stones[i] + k - 1], k - 1)
            if stones[i] + k + 1 in dic and (stones[i] + k + 1, k + 1) not in cache:
                temp |= dp(dic[stones[i] + k + 1], k + 1)
            cache[(i, k)] = temp
            return temp

        return dp(1, 1) if stones[0] + 1 == stones[1] else False
