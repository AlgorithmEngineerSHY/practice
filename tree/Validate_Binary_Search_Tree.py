# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def __init__(self):
        self.if_valisd = True
    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if not root:
            return self.if_valisd

        self.helper(root)
        return self.if_valisd

    def helper(self, node):
        if not self.if_valisd:
            return None, None
        left_min, right_max = None, None

        if node.left:
            if node.left.val >= node.val:
                self.if_valisd = False
                return None, None
            left_min, left_max = self.helper(node.left)
        else:
            left_max = -float('inf')
        if node.right:
            if node.val >= node.right.val:
                self.if_valisd = False
                return None, None
            right_min, right_max = self.helper(node.right)
        else:
            right_min = float('inf')
        if left_max >= node.val or right_min <= node.val:
            self.if_valisd = False
            return None, None
        if not left_min:
            left_min = node.val
        if not right_max:
            right_max = node.val
        return left_min, right_max



