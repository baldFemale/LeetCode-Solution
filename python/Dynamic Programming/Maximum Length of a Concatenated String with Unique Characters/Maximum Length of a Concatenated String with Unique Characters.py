class Solution(object):
    def maxLength(self, arr):
        """
        :type arr: List[str]
        :rtype: int
        """

        dp = [set()]

        for i in arr:
            if len(set(i)) != len(i):
                continue

            for c in dp:
                if set(i) & c:
                    continue
                else:
                    dp.append(set(i) | c)
        return max(len(i) for i in dp)
