class Solution(object):
    def numSubarraysWithSum(self, A, S):
        """
        :type A: List[int]
        :type S: int
        :rtype: int
        """
        dic = {0: 1}
        temp = 0
        res = 0
        for i in range(len(A)):
            temp += A[i]
            if temp - S in dic:
                res += dic[temp - S]
            dic[temp] = dic.get(temp, 0) + 1
        return res
