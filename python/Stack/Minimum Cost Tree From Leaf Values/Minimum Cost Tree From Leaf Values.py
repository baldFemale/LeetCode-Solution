class Solution(object):
    def mctFromLeafValues(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        stack = [float("inf")]

        res = 0

        for i in arr:
            while i > stack[-1]:
                node = stack.pop()
                res += min(i, stack[-1]) * node
            stack.append(i)

        while len(stack) > 2:
            res += stack.pop() * stack[-1]
        return res
