class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

from functools import cmp_to_key
from copy import deepcopy
class Solution:
    def __init__(self):
        self.res = []

    def FindPath(self, root, expectNumber):
        if not root:
            return []
        self.helper(root, expectNumber, [])
        func = lambda x, y: len(x) - len(y)
        self.res = sorted(self.res, key=cmp_to_key(func), reverse=True)
        # self.res = sorted(self.res, cmp=func, reverse=True)

        return self.res

    def helper(self, node, target, path):
        target -= node.val
        path += [node.val]
        if not node.left and not node.right:
            if target == 0:
                self.res.append(path)
        if node.left:
            self.helper(node.left, target, deepcopy(path))
        if node.right:
            self.helper(node.right, target, deepcopy(path))
obj = Solution()
a = TreeNode(1)
a.left = TreeNode(2)
a.right = TreeNode(1)
a.right.right=TreeNode(1)
print(obj.FindPath(a, 3))