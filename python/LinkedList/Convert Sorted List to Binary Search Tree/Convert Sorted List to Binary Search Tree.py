# using recommend order 5 : 876 Middle of the Linked List to find the middle node as current root TreeNode

# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution(object):
    def findMiddleNode(self, head):
        if not head:
            return None, None
        if not head.next:
            return head, None
        slow = head
        fast = head
        pre = slow
        while fast and fast.next:
            pre = slow
            slow = slow.next
            fast = fast.next.next
        pre.next = None
        return head, slow

    def sortedListToBST(self, head):
        """
        :type head: ListNode
        :rtype: TreeNode
        """
        start, middle = self.findMiddleNode(head)
        if not middle:
            if start:
                node = TreeNode(start.val)
                return node
            else:
                return
        node = TreeNode(middle.val)
        node.left = self.sortedListToBST(start)
        node.right = self.sortedListToBST(middle.next)
        return node
