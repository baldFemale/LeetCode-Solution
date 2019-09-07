import bisect


class Solution:
    def shortestDistanceColor(self, colors, queries):
        """
        :type colors: List[int]
        :type queries: List[List[int]]
        :rtype: List[int]
        """
        dic = {
            1: [],
            2: [],
            3: []
        }

        for i, j in enumerate(colors):
            if j == 1:
                dic[1].append(i)
            elif j == 2:
                dic[2].append(i)
            else:
                dic[3].append(i)
        res = []
        for q in queries:
            index, color = q[0], q[1]
            if len(dic[color]) == 0:
                res.append(-1)
            elif colors[index] == color:
                res.append(0)
            else:
                i = bisect.bisect(dic[color], index)
                if i == 0:
                    res.append(dic[color][0] - index)
                elif i == len(dic[color]):
                    res.append(index - dic[color][-1])
                else:
                    res.append(min(index - dic[color][i - 1], dic[color][i] - index))
        return res

