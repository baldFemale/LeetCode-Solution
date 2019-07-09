# using findMiddle in recommend order 5: 876 Middle of the Linked List and reverseList in recommend
# order 7: 206 Reverse Linked List

# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def reorderList(self, head):
        """
        :type head: ListNode
        :rtype: None Do not return anything, modify head in-place instead.
        """

        def findMiddle(head):
            pre = None
            slow = head
            fast = head
            while slow and fast and fast.next:
                pre = slow
                slow = slow.next
                fast = fast.next.next

            pre.next = None
            return head, slow

        def reverse(head):
            pre = None
            while head:
                temp = head.next
                head.next = pre
                pre = head
                head = temp
            return pre

        def merge(head1, head2):
            dummy = ListNode(0)
            cur = dummy
            while head1 and head2:
                cur.next = head1
                cur = cur.next
                head1 = head1.next
                cur.next = head2
                cur = cur.next
                head2 = head2.next
            if head2:
                cur.next = head2
            return dummy.next

        if not head or not head.next:
            return head
        left, right = findMiddle(head)
        head = merge(left, reverse(right))