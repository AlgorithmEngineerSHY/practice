
# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def __init__(self):
        self.re = True

    def isBalanced(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if not root:
            return True
        else:
            self.helper(root)
        return self.re

    def helper(self, node):
        if not node:
            return 0
        left_len = self.helper(node.left)
        if not self.re:
            return None

        right_len = self.helper(node.right)
        if not self.re:
            return None
        delta_len = abs(left_len - right_len)
        if delta_len > 1:
            self.re = False
            return None
        else:
            return max(left_len, right_len) + 1
