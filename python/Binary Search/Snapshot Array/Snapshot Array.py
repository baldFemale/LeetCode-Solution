import bisect


class SnapshotArray(object):

    def __init__(self, length):
        """
        :type length: int
        """
        self.snap_id = 0
        self.array = [[[-1, 0]] for i in range(length)]

    def set(self, index, val):
        """
        :type index: int
        :type val: int
        :rtype: None
        """
        self.array[index].append([self.snap_id, val])

    def snap(self):
        """
        :rtype: int
        """
        self.snap_id += 1
        return self.snap_id - 1

    def get(self, index, snap_id):
        """
        :type index: int
        :type snap_id: int
        :rtype: int
        """
        i = bisect.bisect(self.array[index], [snap_id + 1, 0]) - 1
        return self.array[index][i][1]

# Your SnapshotArray object will be instantiated and called as such:
# obj = SnapshotArray(length)
# obj.set(index,val)
# param_2 = obj.snap()
# param_3 = obj.get(index,snap_id)
