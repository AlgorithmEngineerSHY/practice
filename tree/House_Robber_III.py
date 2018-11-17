# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:

    def rob(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0

        return max(self.helper(root))


    def helper(self, node):
        if not node:
            return 0, 0
        one_left, zero_left = self.helper(node.left)
        one_right, zero_right = self.helper(node.right)
        # 1
        res_1 = node.val + zero_left + zero_right

        # 0
        res_0 = max(zero_left + zero_right, zero_left + one_right, one_left + zero_right, one_left + one_right)

        return res_1, res_0
