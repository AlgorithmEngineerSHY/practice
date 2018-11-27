# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def __init__(self):
        self.first_min = None
        self.stack = []

    def findSecondMinimumValue(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.first_min = root.val
        self.dfs(root)
        return min(self.stack) if self.stack else -1

    def dfs(self, node):
        if node.val == self.first_min:
            if node.left:
                self.dfs(node.left)
                self.dfs(node.right)
        else:
            self.stack.append(node.val)
            return None

