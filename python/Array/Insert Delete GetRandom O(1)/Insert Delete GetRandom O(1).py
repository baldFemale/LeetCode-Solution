from random import randint


class RandomizedSet(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.dic = {}
        self.arr = []
        self.length = 0

    def insert(self, val):
        """
        Inserts a value to the set. Returns true if the set did not already contain the specified element.
        :type val: int
        :rtype: bool
        """
        if val in self.dic:
            return False
        else:
            self.dic[val] = self.length
            self.length += 1
            self.arr.append(val)
            return True

    def remove(self, val):
        """
        Removes a value from the set. Returns true if the set contained the specified element.
        :type val: int
        :rtype: bool
        """
        if val in self.dic:
            if self.dic[val] != self.length - 1:
                index = self.dic[val]
                new_val = self.arr.pop()
                self.arr[index] = new_val
                self.dic[new_val] = index
                del (self.dic[val])
                self.length -= 1
                return True
            else:
                self.arr.pop()
                del (self.dic[val])
                self.length -= 1
                return True
        else:
            return False

    def getRandom(self):
        """
        Get a random element from the set.
        :rtype: int
        """
        index = randint(0, self.length - 1)
        return self.arr[index]

# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()
