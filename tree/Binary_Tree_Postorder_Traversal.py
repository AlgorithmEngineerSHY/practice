'''
Given a binary tree,
return the postorder traversal of its nodes' values.
'''


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def postorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        re, stack = [], [(root, False)]
        while stack:
            node, visited = stack.pop()
            if node:
                if visited is True:
                    re.append(node.val)
                else:
                    stack.append((node, True))
                    stack.append((node.right, False))
                    stack.append((node.left, False))
        return re



