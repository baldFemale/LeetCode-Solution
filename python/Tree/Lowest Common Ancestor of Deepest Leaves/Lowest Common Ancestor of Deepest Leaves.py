# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def lcaDeepestLeaves(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """

        def recur(node):
            if not node:
                return 0, None
            d1, left = recur(node.left)
            d2, right = recur(node.right)

            if d1 < d2:
                temp = right
            elif d1 > d2:
                temp = left
            else:
                temp = node
            return max(d1, d2) + 1, temp

        return recur(root)[1]




