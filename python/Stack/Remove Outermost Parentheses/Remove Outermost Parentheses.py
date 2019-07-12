class Solution(object):
    def removeOuterParentheses(self, S):
        """
        :type S: str
        :rtype: str
        """
        stack = []

        res = ""
        for i in range(len(S)):
            char = S[i]
            if char == "(":
                stack.append(i)
            else:
                pre = stack.pop()
                if not stack:
                    res += S[pre + 1:i]
        return res
