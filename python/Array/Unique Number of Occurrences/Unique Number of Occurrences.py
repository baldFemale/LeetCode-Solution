from collections import Counter


class Solution(object):
    def uniqueOccurrences(self, arr):
        """
        :type arr: List[int]
        :rtype: bool
        """
        c = Counter(arr)

        return len(c.values()) == len(set(c.values()))
