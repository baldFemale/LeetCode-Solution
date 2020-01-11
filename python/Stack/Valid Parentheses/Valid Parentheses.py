class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for ch in s:
            if not stack:
                stack.append(ch)
            else:
                if ch == ")" and stack[-1] == "(":
                    stack.pop()
                elif ch == "]" and stack[-1] == "[":
                    stack.pop()
                elif ch == "}" and stack[-1] == "{":
                    stack.pop()
                else:
                    stack.append(ch)
        return len(stack) == 0
