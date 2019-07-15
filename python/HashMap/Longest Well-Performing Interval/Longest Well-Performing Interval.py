class Solution(object):
    def longestWPI(self, hours):
        """
        :type hours: List[int]
        :rtype: int
        """
        res = 0
        dic = {}
        score = 0

        for i in range(len(hours)):
            if hours[i] > 8:
                score += 1
            else:
                score -= 1
            if score > 0:
                res = max(res, i + 1)

            if score not in dic:
                dic[score] = i

            if score - 1 in dic:
                res = max(res, i - dic[score - 1])
        return res
