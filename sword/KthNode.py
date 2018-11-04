class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def __init__(self):
        self.list_ = []

    def KthNode(self, pRoot, k):
        if k == 0:
            return None
        self.helper(pRoot)
        if k > len(self.list_):
            return None
        return self.list_[k - 1]


    def helper(self, node):
        if node:
            self.helper(node.left)
            self.list_.append(node)
            self.helper(node.right)

obj = Solution()
a = TreeNode(0)
a.left = TreeNode(1)
print(obj.KthNode(a, 2))