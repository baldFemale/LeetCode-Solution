# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def btreeGameWinningMove(self, root, n, x):
        """
        :type root: TreeNode
        :type n: int
        :type x: int
        :rtype: bool
        """

        self.left = 0
        self.right = 0

        def count(node):
            if not node:
                return 0
            l = count(node.left)
            r = count(node.right)
            if node.val == x:
                self.left = l
                self.right = r
            return l + r + 1

        c = count(root)
        return max(self.left, self.right, c - self.left - self.right - 1) > (c // 2)
