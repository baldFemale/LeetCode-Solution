class Solution(object):
    def canThreePartsEqualSum(self, A):
        """
        :type A: List[int]
        :rtype: bool
        """
        s = sum(A)
        if s % 3 != 0:
            return False
        target = s // 3

        cur = 0
        count = 0
        for i in A:
            cur += i
            if cur == target:
                cur = 0
                count += 1
        return count == 3
