class Solution(object):
    def maxSumOfThreeSubarrays(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """

        w = []
        temp = 0
        for i in range(len(nums)):
            temp += nums[i]
            if i >= k:
                temp -= nums[i - k]
            if i >= k - 1:
                w.append(temp)

        left = []
        best = 0
        for i in range(len(w)):
            if w[i] > w[best]:
                best = i
            left.append(best)

        right = [0] * len(w)
        best = len(w) - 1

        for i in range(len(w) - 1, -1, -1):
            if w[i] >= w[best]:
                best = i
            right[i] = best

        ans = None
        res = -float("inf")
        for i in range(k, len(w) - k):
            if w[left[i - k]] + w[right[i + k]] + w[i] > res:
                res = w[left[i - k]] + w[right[i + k]] + w[i]
                ans = [left[i - k], i, right[i + k]]
        return ans
