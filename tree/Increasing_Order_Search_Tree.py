# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def __init__(self):
        self.tree_list = []

    def increasingBST(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        self.helper(root)
        res = TreeNode(0)
        p = res
        for node in self.tree_list:
            p.right = node
            p = p.right
            p.left = None
        return res.right

    def helper(self, node):
        if node.left:
            self.helper(node.left)
        self.tree_list.append(node)
        if node.right:
            self.helper(node.right)
