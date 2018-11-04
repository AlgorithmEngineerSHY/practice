class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
class Solution:
    def reConstructBinaryTree(self, pre, tin):
        if len(pre) == 0:
            return None
        if len(pre) == 1:
            return TreeNode(pre[0])
        node = TreeNode(pre[0])
        idx = tin.index(pre[0])
        node.left = self.reConstructBinaryTree(pre[1: idx + 1], tin[: idx])
        node.right = self.reConstructBinaryTree(pre[idx + 1:], tin[idx + 1:])
        return node


