# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def __init__(self):
        self.L = None
        self.R = None

    def trimBST(self, root, L, R):
        """
        :type root: TreeNode
        :type L: int
        :type R: int
        :rtype: TreeNode
        """
        if not root:
            return None
        self.L = L
        self.R = R
        return self.helper(root)

    def helper(self, node):
        if self.L <= node.val <= self.R:
            if node.left:
                node.left = self.helper(node.left)
            if node.right:
                node.right = self.helper(node.right)
            return node
        elif node.val < self.L:
            if node.right:
                return self.helper(node.right)
        else:
            if node.left:
                return self.helper(node.left)

tree = TreeNode(1)
# tree.left = TreeNode(0)
tree.right = TreeNode(2)
obj = Solution()
nmsl = obj.trimBST(tree, 2, 4)
print(nmsl.val)
# print(nmsl.right.val)
