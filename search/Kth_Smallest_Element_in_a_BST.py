# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def __init__(self):
        self.stack = []

    def kthSmallest(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: int
        """
        self.inner_ergodic(root)
        return self.stack[k - 1]

    def inner_ergodic(self, node):
        if not node:
            return None
        else:
            self.inner_ergodic(node.left)
            self.stack.append(node.val)
            self.inner_ergodic(node.right)
