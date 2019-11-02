class Solution(object):
    def transformArray(self, arr):
        """
        :type arr: List[int]
        :rtype: List[int]
        """
        pre = None

        while pre != arr:
            pre = list(arr)
            temp = list(arr)
            for i in range(1, len(arr) - 1):
                if arr[i] < arr[i + 1] and arr[i] < arr[i - 1]:
                    temp[i] += 1
                elif arr[i] > arr[i + 1] and arr[i] > arr[i - 1]:
                    temp[i] -= 1
            arr = temp
        return arr

