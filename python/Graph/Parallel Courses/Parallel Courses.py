from collections import defaultdict


class Solution(object):
    def minimumSemesters(self, N, relations):
        """
        :type N: int
        :type relations: List[List[int]]
        :rtype: int
        """

        graph = defaultdict(dict)
        temp = defaultdict(dict)

        for i, j in relations:
            graph[i][j] = 1
            temp[j][i] = 1
        indegree = {j: len(temp[j]) for j in temp}
        for i in range(1, N + 1):
            if i not in indegree:
                indegree[i] = 0

        count = 0

        while len(indegree) > 0:
            temp = dict(indegree)
            pop_node = [i for i in temp if temp[i] == 0]
            for i in pop_node:
                for j in graph[i]:
                    temp[j] -= 1
                del (temp[i])
            if len(temp) > 0 and temp == indegree:
                return -1
            else:
                indegree = temp
                count += 1
        return count
