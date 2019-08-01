class Solution(object):
    def distinctSubseqII(self, S):
        """
        :type S: str
        :rtype: int
        """
        dp = [0 for i in range(len(S))]
        dp = [1]+dp
        last = {}
        for i in range(1,len(S)+1):
            dp[i] = dp[i-1]*2
            if S[i-1] in last:
                dp[i]-=dp[last[S[i-1]]-1]
            last[S[i-1]] = i
        return (dp[-1]-1)%(10**9+7)
