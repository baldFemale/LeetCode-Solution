class Solution(object):
    def circularPermutation(self, n, start):
        """
        :type n: int
        :type start: int
        :rtype: List[int]
        """

        def gray(x):
            if x == 1:
                return [0, 1]

            else:
                temp = gray(x - 1)
                return temp + [i + 2 ** (x - 1) for i in temp[::-1]]

        t = gray(n)

        for j, i in enumerate(t):
            if i == start:
                return t[j:] + t[:j]
