from collections import defaultdict


class Solution(object):
    def sortItems(self, n, m, group, beforeItems):
        """
        :type n: int
        :type m: int
        :type group: List[int]
        :type beforeItems: List[List[int]]
        :rtype: List[int]
        """

        def sort_func(gg, indegree):
            res = []
            while len(indegree) > 0:
                temp = dict(indegree)
                pop_node = [i for i in temp.keys() if temp[i] == 0]
                for i in pop_node:
                    for j in gg[i]:
                        if j in temp:
                            temp[j] -= 1
                    res.append(i)
                    del (temp[i])
                if len(temp) > 0 and temp == indegree:
                    return -1
                indegree = temp
            return res

        aggregate = defaultdict(list)
        cur = -1
        group_map = {}

        for i in range(n):
            if group[i] == -1:
                aggregate[cur].append(i)
                group_map[i] = cur
                cur -= 1
            else:
                aggregate[group[i]].append(i)
                group_map[i] = group[i]

        gg = defaultdict(list)
        gf = defaultdict(list)
        print("start")
        for i in range(n):
            if len(beforeItems[i]) > 0:
                for j in beforeItems[i]:
                    if group_map[j] != group_map[i]:
                        gg[group_map[j]].append(group_map[i])
                        gf[group_map[i]].append(group_map[j])
        indegree = {k: len(gf[k]) for k in aggregate.keys()}
        res = sort_func(gg, indegree)
        if res == -1:
            return []
        print(res)

        final_res = []
        for ii in res:
            innernode = aggregate[ii]
            gg = defaultdict(list)
            gf = defaultdict(list)

            for i in innernode:
                if len(beforeItems[i]) > 0:
                    for j in beforeItems[i]:
                        if group_map[j] == group_map[i]:
                            gg[j].append(i)
                            gf[i].append(j)

            indegree = {k: len(gf[k]) for k in innernode}
            res = sort_func(gg, indegree)
            if res == -1:
                return []
            else:
                final_res += res
        return final_res

