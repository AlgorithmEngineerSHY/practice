# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def __init__(self):
        self.values = []

    def minDiffInBST(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.dfs(root)
        min_val = float('inf')
        for i in range(len(self.values) - 1):
            min_val = min(min_val, self.values[i + 1] - self.values[i])
        return min_val


    def dfs(self, node):
        if node.left:
            self.dfs(node.left)
        self.values.append(node.val)
        if node.right:
            self.dfs(node.right)
