class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: bool
        """
        if not nums:
            return False
        left = 0
        right = len(nums) - 1

        while left < right:
            mid = (left + right) // 2
            if target == nums[mid]:
                return True
            if nums[left] == nums[right] == nums[mid]:
                left += 1
                right -= 1
            else:

                if nums[mid] >= nums[left]:
                    if nums[left] <= target < nums[mid]:
                        right = mid - 1
                    else:
                        left = mid + 1
                else:
                    if nums[mid] < target <= nums[right]:
                        left = mid + 1
                    else:
                        right = mid - 1

        print(left, right)
        if nums[left] == target:
            return True
        return False
