# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution(object):
    def mergeList(self, h1, h2):
        pre = ListNode(0)
        cur = pre
        while h1 and h2:
            if h1.val <= h2.val:
                cur.next = h1
                h1 = h1.next
            else:
                cur.next = h2
                h2 = h2.next
            cur = cur.next
        if h1:
            cur.next = h1
        if h2:
            cur.next = h2
        return pre.next

    def sortList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head:
            return
        if not head.next:
            return head

        slow = head
        pre = slow
        fast = head

        while fast and fast.next:
            pre = slow
            fast = fast.next.next
            slow = slow.next
        pre.next = None
        return self.mergeList(self.sortList(head), self.sortList(slow))