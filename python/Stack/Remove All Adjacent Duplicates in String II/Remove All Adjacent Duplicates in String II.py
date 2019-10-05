class Solution(object):
    def removeDuplicates(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: str
        """
        stack = []
        for i in s:
            # print(stack)
            if not stack or stack[-1][0] != i:
                stack.append((i, 1))

            else:
                count = stack[-1][-1] + 1
                if count == k:
                    stack = stack[:-k + 1]
                else:
                    stack.append((i, count))
        return "".join([i[0] for i in stack])
