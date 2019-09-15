class Solution(object):
    def kConcatenationMaxSum(self, arr, k):
        """
        :type arr: List[int]
        :type k: int
        :rtype: int
        """
        v = -float("inf")
        m = 0
        res = v
        cur = 0
        temp = [0]
        for j, i in enumerate(arr):
            temp.append(temp[-1] + i)
            cur = max(cur + i, i)
            m = max(cur, m)
        res = max(res, m)
        print(res)
        cross_m = v

        for i in temp:
            if i <= temp[-1]:
                cross_m = max(cross_m, temp[-1] - i)
        print(cross_m)

        if temp[-1] > 0:
            res = max(res, cross_m + (k - 1) * temp[-1])
        print(res)
        res = max(res, cross_m + max(temp[1:]))
        print(res)
        res = max(res, cross_m + (k - 2) * temp[-1] + max(temp[1:]))
        return res % (10 ** 9 + 7)
