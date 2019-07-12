class Solution(object):
    def nextGreaterElement(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        dic = {}
        stack = []

        for i in nums2:
            if not stack or i < stack[-1]:
                stack.append(i)
            else:
                while stack and stack[-1] < i:
                    pre = stack.pop()
                    dic[pre] = i
                stack.append(i)
        return [dic[i] if i in dic else -1 for i in nums1]