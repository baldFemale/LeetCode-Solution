class Solution(object):
    def maximumSum(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        n = len(arr)
        fw = [0] * n
        bw = [0] * n

        cur_max = -2 ** 32
        max_sofar = -2 * 32
        fans = -2 ** 32
        for i in range(n):
            cur_max = max(cur_max + arr[i], arr[i])
            fw[i] = cur_max
            max_sofar = max(max_sofar, cur_max)
        fans = max(fans, max_sofar)
        cur_max = arr[-1]
        max_sofar = arr[-1]
        bw[-1] = arr[-1]
        i = n - 2
        while i >= 0:
            cur_max = max(arr[i], cur_max + arr[i])
            max_sofar = max(max_sofar, cur_max)
            bw[i] = cur_max
            i -= 1
        fans = max(fans, max_sofar)
        for i in range(1, n - 1):
            fans = max(fans, fw[i - 1] + bw[i + 1])
        return fans
