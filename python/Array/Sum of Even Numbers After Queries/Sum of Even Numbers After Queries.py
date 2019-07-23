class Solution(object):
    def sumEvenAfterQueries(self, A, queries):
        """
        :type A: List[int]
        :type queries: List[List[int]]
        :rtype: List[int]
        """
        ans = sum([i for i in A if i%2==0])
        res = []
        for v,i in queries:
            if A[i]%2==0:
                ans-=A[i]
            A[i]+=v
            if A[i]%2==0:
                ans+=A[i]
            res.append(ans)
        return res
