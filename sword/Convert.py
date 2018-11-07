class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def __init__(self):
        self.res = []

    def Convert(self, pRootOfTree):
        if not pRootOfTree:
            return None
        self.helper(pRootOfTree)
        if len(self.res) == 1:
            return pRootOfTree
        self.res[0].right = self.res[1]

        for i in range(1, len(self.res) - 1):
            self.res[i].left = self.res[i - 1]
            self.res[i].right = self.res[i + 1]
        self.res[-1].left = self.res[-2]
        return self.res[0]

    def helper(self, node):
        if not node.left and not node.right:
            self.res.append(node)
            return None
        if node.left:
            self.helper(node.left)
        self.res.append(node)
        if node.right:
            self.helper(node.right)
