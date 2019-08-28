class Solution(object):
    def brokenCalc(self, X, Y):
        """
        :type X: int
        :type Y: int
        :rtype: int
        """
        if Y>X:
            return Y%2+1+self.brokenCalc(X,(Y+1)//2)
        else:
            return X-Y
