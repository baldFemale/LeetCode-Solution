from collections import Counter
from itertools import product
from itertools import compress


class Solution(object):
    def findNumOfValidWords(self, words, puzzles):
        """
        :type words: List[str]
        :type puzzles: List[str]
        :rtype: List[int]
        """
        c = Counter("".join(sorted(set(w))) for w in words)
        res = []
        for p in puzzles:
            count = 0
            for selec in product([1, 0], repeat=len(p) - 1):
                s = compress(p, [1] + list(selec))
                count += c["".join(sorted(set(s)))]
            res.append(count)
        return res
