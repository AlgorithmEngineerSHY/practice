# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def rightSideView(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if not root:
            return []
        stack = [root]
        res = []
        while stack:
            res.append(stack[-1].val)
            tmp_stack = []
            for node in stack:
                if node.left:
                    tmp_stack.append(node.left)
                if node.right:
                    tmp_stack.append(node.right)
            stack = tmp_stack
        return res
