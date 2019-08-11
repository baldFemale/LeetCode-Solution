import bisect
from collections import defaultdict


class MajorityChecker(object):

    def __init__(self, arr):
        """
        :type arr: List[int]
        """
        self.d = defaultdict(list)
        for i, j in enumerate(arr):
            self.d[j].append(i)

    def query(self, left, right, threshold):
        """
        :type left: int
        :type right: int
        :type threshold: int
        :rtype: int
        """
        for k, v in self.d.items():
            if len(v) < threshold:
                continue
            left_index = bisect.bisect_left(v, left)
            right_index = bisect.bisect_right(v, right)
            if right_index - left_index >= threshold:
                return k
        return -1

# Your MajorityChecker object will be instantiated and called as such:
# obj = MajorityChecker(arr)
# param_1 = obj.query(left,right,threshold)
