# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution(object):
    def reverseBetween(self, head, m, n):
        """
        :type head: ListNode
        :type m: int
        :type n: int
        :rtype: ListNode
        """

        if not head or not head.next:
            return head

        start = head
        pre = None

        while m > 1:
            pre = start
            start = start.next
            m -= 1
            n -= 1

        pre_ = None
        cur = start
        while n:
            temp = cur.next
            cur.next = pre_
            pre_ = cur
            cur = temp
            n -= 1
        if start:
            start.next = temp
        if pre:
            pre.next = pre_
            return head
        else:
            return pre_

