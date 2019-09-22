class Solution(object):
    def nthUglyNumber(self, n, a, b, c):
        """
        :type n: int
        :type a: int
        :type b: int
        :type c: int
        :rtype: int
        """

        def gcd(a, b):
            if b == 0:
                return a
            else:
                return gcd(b, a % b)

        ab = a * b // gcd(a, b)
        ac = a * c // gcd(a, c)
        bc = b * c // gcd(b, c)
        abc = ab * c // gcd(ab, c)

        low = 1
        high = 2 * 10 ** 9

        while low < high:
            mid = (low + high) // 2

            count = mid // a + mid // b + mid // c - mid // ab - mid // ac - mid // bc + mid // abc

            if count < n:
                low = mid + 1
            else:
                high = mid
        return low
