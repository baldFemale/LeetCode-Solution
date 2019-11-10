class Solution(object):
    def reconstructMatrix(self, upper, lower, colsum):
        """
        :type upper: int
        :type lower: int
        :type colsum: List[int]
        :rtype: List[List[int]]
        """

        if upper + lower != sum(colsum):
            return []

        if max(upper, lower) > sum([1 if i > 0 else 0 for i in colsum]):
            return []

        if max(colsum) > sum([1 if i > 0 else 0 for i in [upper, lower]]):
            return []

        u = []
        l = []
        u_count = sum([1 if i == 2 else 0 for i in colsum])
        l_count = int(u_count)

        for i in range(len(colsum)):
            if colsum[i] == 2:
                u.append(1)
                l.append(1)
            elif colsum[i] == 0:
                u.append(0)
                l.append(0)

            else:
                if u_count < upper:
                    u.append(1)
                    l.append(0)
                    u_count += 1
                else:
                    l.append(1)
                    u.append(0)
                    l_count += 1
        return [u, l]