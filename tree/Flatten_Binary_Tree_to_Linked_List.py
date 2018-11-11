# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def __init__(self):
        self.res = []


    def flatten(self, root):
        """
        :type root: TreeNode
        :rtype: void Do not return anything, modify root in-place instead.
        """
        if not root:
            return None
        self.helper(root)
        first = TreeNode(0)
        p = first
        for node in self.res:
            node.left = None
            node.right = None
            p.right = node
            p = p.right
        root = first.right

    def helper(self, node):
        if node:
            self.res.append(node)
            self.helper(node.left)
            self.helper(node.right)
