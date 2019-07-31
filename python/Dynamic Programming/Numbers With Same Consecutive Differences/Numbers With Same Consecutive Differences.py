class Solution(object):
    def numsSameConsecDiff(self, N, K):
        """
        :type N: int
        :type K: int
        :rtype: List[int]
        """
        cur = [i for i in range(1,10)]
        if N==1:
            return [0]+cur
        while N>1:
            temp = []
            N-=1
            for i in cur:
                last = i%10
                if last+K<10:
                    temp.append(i*10+K+last)
                if last-K>=0:
                    temp.append(i*10-K+last)
            cur = list(set(temp))
        return cur
