class Solution(object):
    def calPoints(self, ops):
        """
        :type ops: List[str]
        :rtype: int
        """
        stack = []

        for op in ops:
            if op.isdigit() or op[0] == "-":
                stack.append(int(op))
            else:
                if op == "C":
                    stack.pop()
                if op == "D":
                    stack.append(stack[-1] * 2)
                if op == "+":
                    stack.append(stack[-1] + stack[-2])
        return sum(stack)