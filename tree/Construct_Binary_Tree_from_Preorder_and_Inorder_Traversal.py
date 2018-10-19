# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
from collections import deque
class Solution(object):
    def __init__(self):
        self.pre = None
    def buildTree(self, preorder, inorder):
        """
        :type preorder: List[int]
        :type inorder: List[int]
        :rtype: TreeNode
        """
        self.pre = deque(preorder)
        return self.helper(inorder)

    def helper(self, inorder):
        if inorder:
            p_val = self.pre.popleft()
            idx = inorder.index(p_val)
            root = TreeNode(p_val)
            root.left = self.helper(inorder[:idx])
            root.right = self.helper(inorder[(idx + 1):])
            return root
