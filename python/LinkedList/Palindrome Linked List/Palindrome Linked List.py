# using algorithm in 876 "Middle of the Linked List" and 206 "Reverse Linked List"

# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution(object):
    def reverse(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        pre = None
        while head:
            temp = head.next
            head.next = pre
            pre = head
            head = temp
        return pre

    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        slow = head
        fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        reverse_head = self.reverse(slow)

        while reverse_head:
            if head.val != reverse_head.val:
                return False
            head = head.next
            reverse_head = reverse_head.next
        return True
