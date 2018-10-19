# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

from collections import deque
class Solution(object):
    def __init__(self):
        self.pos = None

    def buildTree(self, inorder, postorder):
        """
        :type inorder: List[int]
        :type postorder: List[int]
        :rtype: TreeNode
        """
        self.pos = deque(postorder)
        return self.helper(inorder)

    def helper(self, inorder):
        if inorder:
            val_p = self.pos.pop()
            print(val_p)
            print('nmsl',inorder)
            idx = inorder.index(val_p)
            root = TreeNode(val_p)
            root.right = self.helper(inorder[(idx + 1):])
            root.left = self.helper(inorder[:idx])

            return root

ogj = Solution()
ogj.buildTree([9,3,15,20,7], [9,15,7,20,3])