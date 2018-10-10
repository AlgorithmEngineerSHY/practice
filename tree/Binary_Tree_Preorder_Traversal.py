'''
Given a binary tree,
return the preorder traversal of its nodes' values.
'''


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def preorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        re, stack = [], [root]
        while stack:
            node = stack.pop()
            if node:
                re.append(node.val)
                stack.append(node.right)
                stack.append(node.left)
        return re