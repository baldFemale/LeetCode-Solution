class Solution(object):
    def numPrimeArrangements(self, n):
        """
        :type n: int
        :rtype: int
        """

        def helper(x):
            if x == 1:
                return 1
            else:
                return x * helper(x - 1)

        prime = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]
        count = 0
        for i in prime:
            if i <= n:
                count += 1
        if count == 0:
            return helper(n) % (10 ** 9 + 7)
        elif count == n:
            return helper(count) % (10 ** 9 + 7)
        return (helper(count) * helper(n - count)) % (10 ** 9 + 7)
