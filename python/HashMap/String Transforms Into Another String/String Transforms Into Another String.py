class Solution(object):
    def canConvert(self, str1, str2):
        """
        :type str1: str
        :type str2: str
        :rtype: bool
        """
        if str1 == str2:
            return True
        dic = {}

        for i, j in zip(str1, str2):
            if dic.setdefault(i, j) != j:
                return False
        return len(set(dic.values())) < 26
