class Solution(object):
    def maxChunksToSorted(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        mi_value = float("inf")
        ma_value = -mi_value
        mi = []
        ma = []

        for i in range(len(arr)):
            ma_value = max(ma_value, arr[i])
            ma.append(ma_value)
        for i in range(len(arr) - 1, -1, -1):
            mi_value = min(mi_value, arr[i])
            mi.append(mi_value)
        mi = mi[::-1]
        print(mi)
        print(ma)
        res = 0
        for i in range(len(arr) - 1):
            if mi[i + 1] >= ma[i]:
                res += 1
        return res + 1
