# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def __init__(self):
        self.leaves_1 = []
        self.leaves_2 = []
        self.mark = None

    def leafSimilar(self, root1, root2):
        """
        :type root1: TreeNode
        :type root2: TreeNode
        :rtype: bool
        """
        self.mark = 1
        self.dfs(root1)
        self.mark = 2
        self.dfs(root2)
        return ''.join(list(map(str, self.leaves_1))) == ''.join(list(map(str, self.leaves_2)))

    def dfs(self, node):
        if not node.left and not node.right:
            if self.mark == 1:
                self.leaves_1.append(node.val)
            else:
                self.leaves_2.append(node.val)
            return None
        if node.left:
            self.dfs(node.left)
        if node.right:
            self.dfs(node.right)

