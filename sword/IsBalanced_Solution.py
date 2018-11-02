class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def __init__(self):
        self.res = True

    def IsBalanced_Solution(self, pRoot):
        len_ = self.helper(pRoot)
        return self.res

    def helper(self, node):
        if not node:
            return 0
        left_height = self.helper(node.left)
        if not self.res:
            return None
        right_height = self.helper(node.right)
        if not self.res:
            return None
        if abs(left_height - right_height) > 1:
            self.res = False
            return None
        return max(left_height, right_height) + 1