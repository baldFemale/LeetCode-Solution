# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution(object):
    def detectCycle(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        slow = head
        fast = head
        step = 0

        while slow and fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            step += 1
            if slow == fast:
                break
        if not fast or not fast.next:
            return None
        slow2 = head
        index = 0
        while slow != slow2:
            slow = slow.next
            slow2 = slow2.next
            index += 1
        return slow