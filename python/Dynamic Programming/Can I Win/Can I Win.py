class Solution(object):
    def canIWin(self, maxChoosableInteger, desiredTotal):
        """
        :type maxChoosableInteger: int
        :type desiredTotal: int
        :rtype: bool
        """
        cache = {}
        allow = [i + 1 for i in range(maxChoosableInteger)]

        def dfs(allow, value):
            state = tuple(allow)
            if len(allow) == 0:
                cache[state] = False
                return False
            if state in cache:
                return cache[state]
            if value + max(allow) >= desiredTotal:
                cache[state] = True
                return True
            cache[state] = False
            for i in allow:
                temp_allow = [j for j in allow if j != i]
                if dfs(temp_allow, value + i) == False:
                    cache[state] = True
                    break
            return cache[state]

        return dfs(allow, 0) if maxChoosableInteger * (maxChoosableInteger + 1) >= desiredTotal else False
