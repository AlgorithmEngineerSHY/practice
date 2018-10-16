# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def __init__(self):
        self.pre_node = TreeNode(-float('inf'))
        self.first_node = None
        self.second_node = None

    def recoverTree(self, root):
        """
        :type root: TreeNode
        :rtype: void Do not return anything, modify root in-place instead.
        """
        if not root:
            return None
        self.helper(root)
        self.first_node.val, self.second_node.val = self.second_node.val, self.first_node.val


    def helper(self, node):
        if not node:
            return None
        self.helper(node.left)

        if not self.first_node and self.pre_node.val > node.val:
            self.first_node = self.pre_node
        if self.first_node and self.pre_node.val > node.val:
            self.second_node = node
        self.pre_node = node

        self.helper(node.right)
