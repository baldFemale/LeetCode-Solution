class Solution(object):
    def atMostNGivenDigitSet(self, D, N):
        """
        :type D: List[str]
        :type N: int
        :rtype: int
        """
        res = 0

        res += sum(len(D) ** i for i in range(1, len(str(N))))

        i = 0
        while i < len(str(N)):
            res += sum(D[j] < str(N)[i] for j in range(len(D))) * len(D) ** (len(str(N)) - i - 1)

            if str(N)[i] not in D:
                break
            i += 1
        return res + (i == len(str(N)))
