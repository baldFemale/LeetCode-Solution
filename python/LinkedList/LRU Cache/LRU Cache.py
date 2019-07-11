class ListNode(object):

    def __init__(self, val, key=None):
        self.val = val
        self.key = key
        self.next = None
        self.pre = None


class LRUCache(object):

    def __init__(self, capacity):
        """
        :type capacity: int
        """
        self.capacity = capacity
        self.dic = {}
        self.head = ListNode(0)
        self.tail = ListNode(0)
        self.head.next = self.tail
        self.tail.pre = self.head

    def add(self, node):
        pre = self.tail.pre
        pre.next = node
        node.pre = pre
        node.next = self.tail
        self.tail.pre = node

    def remove(self, node):
        pre = node.pre
        _next = node.next
        pre.next = _next
        _next.pre = pre

    def get(self, key):
        """
        :type key: int
        :rtype: int
        """
        if key in self.dic:
            node = self.dic[key]
            self.remove(node)
            self.add(node)
            return node.val
        else:
            return -1

    def put(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: None
        """
        if key in self.dic:
            node = self.dic[key]
            self.remove(node)
        node = ListNode(value, key)
        self.add(node)
        self.dic[key] = node
        if len(self.dic) > self.capacity:
            temp = self.head.next
            self.remove(temp)
            del self.dic[temp.key]

# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
