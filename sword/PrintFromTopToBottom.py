class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
class Solution:
    def PrintFromTopToBottom(self, root):
        if not root:
            return []
        res = []
        stack = [root]

        while stack:
            tmp_stack = []
            for node in stack:
                res.append(node.val)
                if node.left:
                    tmp_stack.append(node.left)
                if node.right:
                    tmp_stack.append(node.right)
            stack = tmp_stack
        return res