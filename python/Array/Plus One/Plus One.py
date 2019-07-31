class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        res = []
        cur = 1
        for d in digits[::-1]:
            res.append((d+cur)%10)
            cur = (d+cur)//10
        if cur:
            res.append(cur)
        return res[::-1]
