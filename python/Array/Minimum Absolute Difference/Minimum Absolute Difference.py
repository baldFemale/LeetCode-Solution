class Solution(object):
    def minimumAbsDifference(self, arr):
        """
        :type arr: List[int]
        :rtype: List[List[int]]
        """
        arr.sort()

        dis = float("inf")

        for i in range(1, len(arr)):
            dis = min(dis, arr[i] - arr[i - 1])

        res = []

        s = set(arr)
        for i in arr:
            if i + dis in s:
                res.append([i, i + dis])
        return res
