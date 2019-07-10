# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def reverseKGroup(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        if not head or not head.next or k == 0 or k == 1:
            return head

        cur = head
        pre_cur = None
        count = 0
        while count < k and cur:
            pre_cur = cur
            cur = cur.next
            count += 1
        if count < k:
            return head

        pre = self.reverseKGroup(cur, k)
        reverse_cur = head

        while count:
            temp = reverse_cur.next
            reverse_cur.next = pre
            pre = reverse_cur
            reverse_cur = temp
            count -= 1
        return pre






