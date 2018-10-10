
# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def __init__(self):
        self.sum_ = None
        self.if_true = False
    def hasPathSum(self, root, sum_):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: bool
        """
        if not root:
            return False
        self.sum_ = sum_
        self.helper(root, 0)
        return self.if_true

    def helper(self, root, tmp_num):
        if self.if_true:
            return None
        tmp_num += root.val
        if not root.left and not root.right:
            if tmp_num == self.sum_:
                self.if_true = True
        else:
            if root.left:
                self.helper(root.left, tmp_num)
            if root.right:
                self.helper(root.right, tmp_num)
