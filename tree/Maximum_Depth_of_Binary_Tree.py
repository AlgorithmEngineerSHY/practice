# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0
        return self.helper(root)


    def helper(self, node):

        if not node.left and not node.right:
            return 1
        left_max, right_max = 0, 0
        if node.left:
            left_max = self.helper(node.left)
        if node.right:
            right_max = self.helper(node.right)
        return max(left_max, right_max) + 1