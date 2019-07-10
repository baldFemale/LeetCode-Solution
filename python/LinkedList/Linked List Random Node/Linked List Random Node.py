# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

import random


class Solution(object):

    def __init__(self, head):
        """
        @param head The linked list's head.
        Note that the head is guaranteed to be not null, so it contains at least one node.
        :type head: ListNode
        """
        self.head = head

    def getRandom(self):
        """
        Returns a random node's value.
        :rtype: int
        """
        cur = self.head
        c = 1
        res = cur.val
        while cur.next:
            cur = cur.next
            c += 1
            r = random.randint(1, c)
            if r == c:
                res = cur.val
        return res

# Your Solution object will be instantiated and called as such:
# obj = Solution(head)
# param_1 = obj.getRandom()