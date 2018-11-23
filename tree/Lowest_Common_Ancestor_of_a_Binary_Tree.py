# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def __init__(self):
        self.res = None
        self.p = None
        self.q = None
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        self.p = p
        self.q = q
        self.post_ergodic(root)
        return self.res


    def post_ergodic(self, node):
        if self.res:
            return False
        if not node:
            return False
        left = self.post_ergodic(node.left)
        right = self.post_ergodic(node.right)

        mid = node == self.p or node == self.q

        if mid + left + right > 1:
            self.res = node

        return mid or left or right

