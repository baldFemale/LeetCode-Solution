class Solution(object):
    def minRemoveToMakeValid(self, s):
        """
        :type s: str
        :rtype: str
        """
        r = []

        stack = []

        for i, j in enumerate(s):
            if j not in ["(", ")"]:
                continue

            if j == "(":
                stack.append(i)

            else:
                if len(stack) == 0:
                    r.append(i)
                else:
                    if s[stack[-1]] == "(":
                        stack.pop()

        r = r + stack
        print(r)
        if len(r) == 0:
            return s
        res = ""
        for i, j in enumerate(r):
            if i == 0:
                res += s[:j]
            else:
                res += s[r[i - 1] + 1:j]

            if i == len(r) - 1:
                res += s[j + 1:]
        return res
