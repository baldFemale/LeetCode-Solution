# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def twoSumBSTs(self, root1, root2, target):
        """
        :type root1: TreeNode
        :type root2: TreeNode
        :type target: int
        :rtype: bool
        """

        def inorder(node):
            if not node:
                return []
            else:
                return inorder(node.left) + [node.val] + inorder(node.right)

        t1 = inorder(root1)
        t2 = inorder(root2)

        i = 0
        j = len(t2) - 1

        while i < len(t1) and j >= 0:
            if t1[i] + t2[j] == target:
                return True
            else:
                if t1[i] + t2[j] > target:
                    j -= 1
                else:
                    i += 1
        return False
