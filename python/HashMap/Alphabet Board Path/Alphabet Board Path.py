class Solution(object):
    def alphabetBoardPath(self, target):
        """
        :type target: str
        :rtype: str
        """
        board = {chr(ord("a") + i * 5 + j): (i, j) for i in range(5) for j in range(5)}
        board["z"] = (5, 0)
        res = ""
        current = (0, 0)
        for i in target:
            cur_x, cur_y = current
            next_x, next_y = board[i]
            if i != "z":
                if next_x >= cur_x:
                    for j in range(next_x - cur_x):
                        res += "D"
                else:
                    for j in range(cur_x - next_x):
                        res += "U"
                if next_y >= cur_y:
                    for j in range(next_y - cur_y):
                        res += "R"
                else:
                    for j in range(cur_y - next_y):
                        res += "L"
            else:
                for j in range(cur_y - next_y):
                    res += "L"
                for j in range(next_x - cur_x):
                    res += "D"

            res += "!"
            current = (next_x, next_y)
        return res
