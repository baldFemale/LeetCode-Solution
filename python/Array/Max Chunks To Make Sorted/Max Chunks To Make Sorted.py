class Solution(object):
    def maxChunksToSorted(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        ma = -float("inf")
        res = 0
        for i in range(len(arr)):
            ma = max(ma,arr[i])
            if ma==i:
                res+=1
        return res
