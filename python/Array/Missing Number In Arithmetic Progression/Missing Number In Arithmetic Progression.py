class Solution(object):
    def missingNumber(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        interval = (arr[-1] - arr[0]) / len(arr)
        if interval == 0:
            return arr[0]

        for i in range(len(arr)):
            if arr[i] + interval != arr[i + 1]:
                return arr[i] + interval
    