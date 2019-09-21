class Solution(object):
    def maxNumberOfApples(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        arr.sort()

        weight = 5000
        count = 0

        while len(arr) > 0 and weight - arr[0] > 0:
            count += 1
            weight -= arr[0]
            arr.pop(0)
        return count
