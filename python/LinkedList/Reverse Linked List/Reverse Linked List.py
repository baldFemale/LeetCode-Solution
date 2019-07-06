# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution(object):
    def reverselist(self, head):
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
