class Solution(object):
    def maximumNumberOfOnes(self, width, height, sideLength, maxOnes):
        """
        :type width: int
        :type height: int
        :type sideLength: int
        :type maxOnes: int
        :rtype: int
        """
        count = [0] * sideLength ** 2

        for i in range(height):
            for j in range(width):
                count[i % sideLength * sideLength + j % sideLength] += 1

        res = 0
        count.sort()
        for i in range(maxOnes):
            res += count.pop()
        return res
