class Solution(object):
    def duplicateZeros(self, arr):
        """
        :type arr: List[int]
        :rtype: None Do not return anything, modify arr in-place instead.
        """

        count = 0
        for i in arr:
            if i == 0:
                count += 1

        for j in range(len(arr) - 1, -1, -1):
            if j + count < len(arr):
                arr[j + count] = arr[j]
            if arr[j] == 0:
                count -= 1
                if j + count < len(arr):
                    arr[j + count] = 0
