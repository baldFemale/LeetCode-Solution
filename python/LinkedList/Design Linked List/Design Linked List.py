class ListNode(object):

    def __init__(self, x):
        self.val = x
        self.next = None
        self.pre = None


class MyLinkedList(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.head = ListNode(0)
        self.tail = ListNode(0)
        self.head.next = self.tail
        self.tail.pre = self.head
        self.length = 0

    def get(self, index):
        """
        Get the value of the index-th node in the linked list. If the index is invalid, return -1.
        :type index: int
        :rtype: int
        """
        if index < 0 or index >= self.length:
            return -1

        cur = self.head
        for i in range(index):
            cur = cur.next
        return cur.next.val

    def addAtHead(self, val):
        """
        Add a node of value val before the first element of the linked list. After the insertion, the new node will be the first node of the linked list.
        :type val: int
        :rtype: None
        """
        node = ListNode(val)
        temp = self.head.next
        self.head.next = node
        node.pre = self.head
        node.next = temp
        temp.pre = node
        self.length += 1

    def addAtTail(self, val):
        """
        Append a node of value val to the last element of the linked list.
        :type val: int
        :rtype: None
        """
        node = ListNode(val)
        temp = self.tail.pre
        self.tail.pre = node
        node.next = self.tail
        node.pre = temp
        temp.next = node
        self.length += 1

    def addAtIndex(self, index, val):
        """
        Add a node of value val before the index-th node in the linked list. If index equals to the length of linked list, the node will be appended to the end of linked list. If index is greater than the length, the node will not be inserted.
        :type index: int
        :type val: int
        :rtype: None
        """
        if index < 0:
            index = 0
        if index < 0 or index > self.length:
            return
        if index == self.length:
            self.addAtTail(val)
            return

        cur = self.head
        node = ListNode(val)
        for i in range(index):
            cur = cur.next
        temp = cur.next
        cur.next = node
        node.next = temp
        temp.pre = node
        node.pre = cur
        self.length += 1
        return

    def deleteAtIndex(self, index):
        """
        Delete the index-th node in the linked list, if the index is valid.
        :type index: int
        :rtype: None
        """
        if index < 0 or index >= self.length:
            return

        cur = self.head
        for i in range(index):
            cur = cur.next
        del_node = cur.next
        del (del_node)
        temp = cur.next.next
        cur.next = temp
        temp.pre = cur
        self.length -= 1
        return

# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)