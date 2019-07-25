from random import randint
from collections import defaultdict


class RandomizedCollection(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.dic = defaultdict(set)
        self.arr = []
        self.length = 0

    def insert(self, val):
        """
        Inserts a value to the collection. Returns true if the collection did not already contain the specified element.
        :type val: int
        :rtype: bool
        """
        self.dic[val].add(self.length)
        self.length += 1
        self.arr.append(val)
        return len(self.dic[val]) == 1

    def remove(self, val):
        """
        Removes a value from the collection. Returns true if the collection contained the specified element.
        :type val: int
        :rtype: bool
        """
        if len(self.dic[val]) >= 1:
            index = self.dic[val].pop()
            last = self.arr[-1]
            self.arr[index] = last
            self.arr.pop()
            self.dic[last].add(index)
            self.dic[last].remove(self.length - 1)
            self.length -= 1
            return True
        else:
            return False

    def getRandom(self):
        """
        Get a random element from the collection.
        :rtype: int
        """
        index = randint(0, self.length - 1)
        return self.arr[index]

# Your RandomizedCollection object will be instantiated and called as such:
# obj = RandomizedCollection()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()
