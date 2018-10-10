# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def __init__(self):
        self.re = []
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if not root:
            return []
        self.helper(root)
        return self.re
    def helper(self, node):
        # if not node:
        #     return None
        if node.left:
            self.helper(node.left)

        self.re.append(node.val)

        if node.right:
            self.helper(node.right)



