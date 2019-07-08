# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        slow = head
        fast = head

        for i in range(n):
            fast = fast.next
        if not fast:
            return slow.next

        while fast and fast.next:
            fast = fast.next
            slow = slow.next
        slow.next = slow.next.next
        return head