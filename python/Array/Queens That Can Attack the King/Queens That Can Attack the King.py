class Solution(object):
    def queensAttacktheKing(self, queens, king):
        """
        :type queens: List[List[int]]
        :type king: List[int]
        :rtype: List[List[int]]
        """
        queens = set([tuple(x) for x in queens])
        res = []

        for i in range(king[1] + 1, 8):
            if (king[0], i) in queens:
                res.append([king[0], i])
                break

        for i in range(king[1] - 1, -1, -1):
            if (king[0], i) in queens:
                res.append([king[0], i])
                break

        for i in range(king[0] + 1, 8):
            if (i, king[1]) in queens:
                res.append([i, king[1]])
                break
        for i in range(king[0] - 1, -1, -1):
            if (i, king[1]) in queens:
                res.append([i, king[1]])
                break

        for i in range(1, min(8 - king[1], 8 - king[0])):
            if (king[0] + i, king[1] + i) in queens:
                res.append([king[0] + i, king[1] + i])
                break
        for i in range(1, min(8 - king[1], king[0] + 1)):
            if (king[0] - i, king[1] + i) in queens:
                res.append([king[0] - i, king[1] + i])
                break

        for i in range(1, min(king[1] + 1, 8 - king[0])):
            if (king[0] + i, king[1] - i) in queens:
                res.append([king[0] + i, king[1] - i])
                break

        for i in range(1, min(king[1] + 1, king[0] + 1)):
            if (king[0] - i, king[1] - i) in queens:
                res.append([king[0] - i, king[1] - i])
                break

        return res
