# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution(object):
    def insertionSortList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """

        pre = ListNode(0)
        pre_cur = pre

        cur = head

        while cur:
            temp = cur.next
            while pre_cur.next and pre_cur.next.val <= cur.val:
                pre_cur = pre_cur.next
            cur.next = pre_cur.next
            pre_cur.next = cur
            pre_cur = pre
            cur = temp
        return pre.next

