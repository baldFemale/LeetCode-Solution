from collections import Counter

class Solution(object):
    def commonChars(self, A):
        """
        :type A: List[str]
        :rtype: List[str]
        """
        c = Counter(A[0])
        for word in A[1:]:
            temp = Counter(word)
            c = c & temp

        res = []
        for k in c:
            res += [k] * c[k]
        return res
