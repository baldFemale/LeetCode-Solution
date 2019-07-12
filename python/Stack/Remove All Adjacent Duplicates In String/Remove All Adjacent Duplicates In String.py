class Solution(object):
    def removeDuplicates(self, S):
        """
        :type S: str
        :rtype: str
        """
        stack = []

        for i in S:
            if not stack or i != stack[-1]:
                stack.append(i)
            else:
                stack.pop()
        return "".join(stack)