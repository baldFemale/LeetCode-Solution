class Solution(object):
    def probabilityOfHeads(self, prob, target):
        """
        :type prob: List[float]
        :type target: int
        :rtype: float
        """
        cache = {}

        def dp(l, n):
            if (l, n) in cache:
                return cache[(l, n)]
            if n > l:
                cache[(l, n)] = 0
                return 0
            else:
                if l == 1:
                    if n == 0:
                        cache[(l, n)] = 1 - prob[0]
                        return 1 - prob[0]
                    else:
                        cache[(l, n)] = prob[0]
                        return prob[0]
                else:
                    if n == 0:
                        cache[(l, n)] = (1 - prob[l - 1]) * dp(l - 1, 0)
                        return cache[(l, n)]

                    else:
                        cache[(l, n)] = (1 - prob[l - 1]) * dp(l - 1, n) + (prob[l - 1]) * dp(l - 1, n - 1)
                        return cache[(l, n)]

        return dp(len(prob), target)
