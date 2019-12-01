class Solution:
    def removeInterval(self, intervals: List[List[int]], toBeRemoved: List[int]) -> List[List[int]]:
        intervals.sort(key=lambda x: x[1])

        res = []

        for i in intervals:
            if i[1] <= toBeRemoved[0]:
                res.append(i)
            else:
                if i[1] <= toBeRemoved[1]:
                    if i[0] < toBeRemoved[0]:
                        res.append([i[0], toBeRemoved[0]])
                    else:
                        pass
                else:
                    if i[0] < toBeRemoved[0]:
                        res.append([i[0], toBeRemoved[0]])
                    if i[0] <= toBeRemoved[1]:
                        res.append([toBeRemoved[1], i[1]])
                    else:
                        res.append(i)
        return res

