# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def longestUnivaluePath(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.res = 0
        self.dfs(root)
        return self.res

    def dfs(self, node):
        if not node:
            return 0
        left_len = self.dfs(node.left)
        right_len = self.dfs(node.right)

        re_left = re_right = 0
        if node.left and node.left.val == node.val:
            re_left = left_len + 1
        if node.right and node.right.val == node.val:
            re_right = right_len + 1
        self.res = max(self.res, re_left + re_right)
        return max(re_left, re_right)