# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution(object):
    def oddEvenList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head:
            return

        odd = head
        even = head.next
        even_start = head.next

        while even and even.next:
            temp = even.next
            odd.next = temp
            odd = odd.next
            even.next = odd.next
            even = even.next
        odd.next = even_start
        return head