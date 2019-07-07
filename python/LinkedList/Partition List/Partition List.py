# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution(object):
    def partition(self, head, x):
        """
        :type head: ListNode
        :type x: int
        :rtype: ListNode
        """
        small_head = ListNode(0)
        small_cur = small_head
        big_head = ListNode(0)
        big_cur = big_head

        while head:
            if head.val >= x:
                big_cur.next = head
                big_cur = big_cur.next
            else:
                small_cur.next = head
                small_cur = small_cur.next
            head = head.next
        big_cur.next = None
        small_cur.next = big_head.next
        return small_head.next

