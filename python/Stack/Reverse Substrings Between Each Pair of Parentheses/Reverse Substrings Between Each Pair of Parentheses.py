class Solution(object):
    def reverseParentheses(self, s):
        """
        :type s: str
        :rtype: str
        """
        stack = []

        for i, j in enumerate(s):
            if j != ")":
                stack.append(j)
            else:
                temp = ""
                while stack[-1] != "(":
                    temp += stack.pop()
                stack.pop()
                for t in temp:
                    stack.append(t)
        return "".join(stack)
