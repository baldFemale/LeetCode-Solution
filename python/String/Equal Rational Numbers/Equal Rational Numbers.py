class Solution(object):
    def isRationalEqual(self, S, T):
        """
        :type S: str
        :type T: str
        :rtype: bool
        """
        def f(s):
            index = s.find("(")
            if index!=-1:
                s = s[:index]+s[index+1:-1]*20
            return s[:20]
        return float(f(S))==float(f(T))
