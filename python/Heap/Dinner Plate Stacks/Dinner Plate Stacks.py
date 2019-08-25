import heapq


class DinnerPlates(object):

    def __init__(self, capacity):
        """
        :type capacity: int
        """
        self.stacks = [[]]
        self.index = [0]
        heapq.heapify(self.index)
        self.capacity = capacity

    def push(self, val):
        """
        :type val: int
        :rtype: None
        """
        i = heapq.heappop(self.index)
        self.stacks[i].append(val)
        if len(self.stacks[i]) < self.capacity:
            heapq.heappush(self.index, i)
        if len(self.index) == 0:
            heapq.heappush(self.index, len(self.stacks))
            self.stacks.append([])

    def pop(self):
        """
        :rtype: int
        """
        while len(self.stacks) >= 1 and len(self.stacks[-1]) == 0:
            self.stacks.pop()
        if len(self.stacks) == 0:
            return -1
        if len(self.stacks[-1]) == self.capacity:
            heapq.heappush(self.index, len(self.stacks) - 1)
        val = self.stacks[-1].pop()
        return val

    def popAtStack(self, index):
        """
        :type index: int
        :rtype: int
        """
        if len(self.stacks[index]) == 0:
            return -1
        if len(self.stacks[index]) == self.capacity:
            heapq.heappush(self.index, index)
        val = self.stacks[index].pop()
        return val

# Your DinnerPlates object will be instantiated and called as such:
# obj = DinnerPlates(capacity)
# obj.push(val)
# param_2 = obj.pop()
# param_3 = obj.popAtStack(index)
