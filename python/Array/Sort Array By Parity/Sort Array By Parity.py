class Solution(object):
    def sortArrayByParity(self, A):
        """
        :type A: List[int]
        :rtype: List[int]
        """
        i = 0
        j = len(A)-1
        while i<j:
            while i<len(A) and A[i]%2==0:
                i+=1
            while j>0 and A[j]%2==1:
                j-=1
            if 0<=i<j<len(A):
                A[i],A[j] = A[j],A[i]
        return A
