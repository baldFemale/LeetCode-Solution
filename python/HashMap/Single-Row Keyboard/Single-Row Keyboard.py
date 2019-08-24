class Solution(object):
    def calculateTime(self, keyboard, word):
        """
        :type keyboard: str
        :type word: str
        :rtype: int
        """
        dic = {keyboard[i]: i for i in range(26)}

        cur = 0
        res = 0
        for c in word:
            res += abs(dic[c] - cur)
            cur = dic[c]
        return res
