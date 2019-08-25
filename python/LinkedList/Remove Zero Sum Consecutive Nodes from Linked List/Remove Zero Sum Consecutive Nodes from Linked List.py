# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def removeZeroSumSublists(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        cur = head

        a = []
        while cur:
            a.append(cur.val)
            cur = cur.next
        res = []
        for i in a:
            if i == 0:
                continue
            else:
                tag = True
                for j in range(len(res) - 1, -1, -1):
                    if sum(res[j:]) + i == 0:
                        res = res[:j]
                        tag = False
                        break
                if tag:
                    res.append(i)

        head = ListNode(0)
        cur = head
        for i in res:
            node = ListNode(i)
            cur.next = node
            cur = cur.next
        return head.next