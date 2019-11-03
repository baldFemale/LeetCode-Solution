class Solution(object):
    def numberOfSubarrays(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        t = []
        for i, j in enumerate(nums):
            if j % 2 == 1:
                t.append(i)

        # print(t)
        if len(t) < k:
            return 0
        res = 0
        for i in range(len(t) - k + 1):
            i1 = t[i]
            i2 = t[i + k - 1]
            # print(i,i1,i2)

            if i + k < len(t) and i > 0:
                res += (t[i + k] - i2) * (i1 - t[i - 1])
            else:
                if i + k == len(t) and i == 0:
                    res += (i1 - 0 + 1) * (len(nums) - i2)
                elif i + k == len(t):
                    res += (i1 - t[i - 1]) * (len(nums) - i2)
                else:
                    res += (t[i + k] - i2) * (i1 - 0 + 1)
        return res
