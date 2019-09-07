class Solution:
    def beforeAndAfterPuzzles(self, phrases):
        """
        :type phrases: List[str]
        :rtype: List[str]
        """
        n = len(phrases)
        res = []
        for i in range(n):
            for j in range(n):
                if i==j:
                    continue
                items_i = phrases[i].split(" ")
                items_j = phrases[j].split(" ")
                if items_i[-1]==items_j[0]:
                    res.append(" ".join(items_i+items_j[1:]))
        return sorted(list(set(res)))