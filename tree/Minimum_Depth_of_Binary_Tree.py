'''
Given a binary tree, find its minimum depth.
The minimum depth is the number of nodes along the shortest path
from the root node down to the nearest leaf node.
'''


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def minDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0
        if not root.left and not root.right:
            return 1
        if not root.left:
            return 1 + self.helper(root.right)
        if not root.right:
            return 1 + self.helper(root.left)
        return self.helper(root)

    def helper(self, root):
        if not root.left and not root.right:
            print('aaa')
            return 1
        # left_min, right_min = float('inf'), float('inf')
        if not root.left:
            right_min = self.helper(root.right)
            return right_min + 1
        if not root.right:
            left_min = self.helper(root.left)
            return left_min + 1
        right_min = self.helper(root.right)
        left_min = self.helper(root.left)
        return min(left_min, right_min) + 1
a=TreeNode(3)
a.left=TreeNode(9)
a.right=TreeNode(20)
a.right.left=TreeNode(15)
a.right.right=TreeNode(7)
b=Solution()
print(b.minDepth(a))