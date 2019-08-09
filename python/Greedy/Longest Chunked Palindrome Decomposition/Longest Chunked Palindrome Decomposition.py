class Solution(object):
    def longestDecomposition(self, text):
        """
        :type text: str
        :rtype: int
        """
        left_pre = 0
        right_pre = len(text)
        left = 1
        right = len(text) - 1
        count = 0

        while left <= right:
            if left > left_pre and right < right_pre and text[left_pre:left] == text[right:right_pre]:
                count += 2
                left_pre = left
                right_pre = right
            left += 1
            right -= 1
        if left_pre < right_pre:
            count += 1
        return count
