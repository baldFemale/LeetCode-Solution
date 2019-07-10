# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def rotateRight(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        if not head or not head.next:
            return head

        c = 1
        cur = head
        while cur.next:
            cur = cur.next
            c += 1
        cur.next = head
        pre = None
        cur = head
        k = k % c
        while c - k > 0:
            c -= 1
            pre = cur
            cur = cur.next
        pre.next = None
        return cur
