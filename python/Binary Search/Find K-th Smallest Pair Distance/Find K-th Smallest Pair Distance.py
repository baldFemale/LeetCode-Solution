class Solution(object):
    def smallestDistancePair(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        nums.sort()

        def count(val):
            c = 0
            left = 0

            for right in range(len(nums)):
                while nums[right] - nums[left] > val:
                    left += 1
                c += right - left
            return c >= k

        low = 0
        high = nums[-1] - nums[0]
        while low < high:
            mid = (low + high) // 2
            if count(mid):
                high = mid
            else:
                low = mid + 1
        return low
