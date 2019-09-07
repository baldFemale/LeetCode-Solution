class Solution(object):
    def countLetters(self, S):
        """
        :type S: str
        :rtype: int
        """
        res = 0
        count = 0
        temp = ""
        for i in S:
            if count==0 or temp[-1]==i:
                count+=1
                temp = temp+i
            else:
                temp = i
                res+=(count*(count+1))//2
                count = 1
        if count:
            res+=(count*(count+1))//2
        return res
