class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
class Solution:
    def TreeDepth(self, pRoot):
        if not pRoot:
            return 0
        return self.helper(pRoot)
    def helper(self, node):
        if not node.left and not node.right:
            return 1
        left, right = 0, 0
        if node.left:
            left = self.helper(node.left)
        if node.right:
            right = self.helper(node.right)
        return max(left, right) + 1

obj = Solution()
tree = TreeNode(0)
tree.left = TreeNode(1)
print(obj.TreeDepth(tree))