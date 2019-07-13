class Solution(object):
    def backspaceCompare(self, S, T):
        """
        :type S: str
        :type T: str
        :rtype: bool
        """

        def backspace(s):
            stack = []
            for i in s:
                if i != "#":
                    stack.append(i)
                else:
                    if stack:
                        stack.pop()
            return "".join(stack)

        return backspace(S) == backspace(T)