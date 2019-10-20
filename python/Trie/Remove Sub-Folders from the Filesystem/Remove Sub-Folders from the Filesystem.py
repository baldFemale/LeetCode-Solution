from collections import defaultdict


class Solution(object):
    def removeSubfolders(self, folder):
        """
        :type folder: List[str]
        :rtype: List[str]
        """
        Trie = lambda: defaultdict(Trie)

        trie = Trie()
        END = True

        # for path in folder:
        #     reduce(dict.__getitem__, path, trie)[END] = path

        for path in folder:
            t = trie
            p = path.split("/")
            # print(p)
            for i in range(1, len(p)):
                if True in t.keys():
                    break
                t = t[p[i]]
            if True not in t.keys():
                t[True] = path
        # print(trie)

        res = set()
        for path in folder:
            temp = "/"
            t = trie
            p = path.split("/")
            for i in p[1:]:
                temp += i
                if True in t[i].keys():
                    res.add(temp)
                    break
                t = t[i]
                temp += "/"
        res = list(res)
        return res

