class Solution(object):
    def maximumProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        m = float("inf")
        min1 = m
        min2 = m
        max1 = -m
        max2 = -m
        max3 = -m

        for i in nums:
            if i < min1:
                min2 = min1
                min1 = i
            elif i < min2:
                min2 = i

            if i > max1:
                max3 = max2
                max2 = max1
                max1 = i
            elif i > max2:
                max3 = max2
                max2 = i
            elif i > max3:
                max3 = i

        return max(min1 * min2, max2 * max3) * max1
