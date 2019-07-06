# similar solution as 876 "Middle of the Linked List"

# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        slow = head
        fast = head

        while fast and fast.next and slow:
            slow = slow.next
            fast = fast.next.next
            if fast == slow:
                return True
        return False
