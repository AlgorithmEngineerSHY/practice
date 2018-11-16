# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def searchBST(self, root, val):
        """
        :type root: TreeNode
        :type val: int
        :rtype: TreeNode
        """
        if not root:
            return None
        self.val = val
        return self.dfs(root)

    def dfs(self, node):
        if not node:
            return None
        elif self.val == node.val:
            return node
        elif self.val > node.val:
            return self.dfs(node.right)
        else:
            return self.dfs(node.left)
