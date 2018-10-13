# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def generateTrees(self, n):
        """
        :type n: int
        :rtype: List[TreeNode]
        """
        if n == 0:
            return []
        if n == 1:
            return [TreeNode(1)]

        return self.helper(1, n)


    def helper(self, start, end):
        if start == end:
            return [TreeNode(start)]
        if start > end:
            return [None]
        re = []
        for i in range(start, end + 1):
            for j in self.helper(start, i - 1):
                for k in self.helper(i + 1, end):
                    node = TreeNode(i)
                    node.left = j
                    node.right = k
                    re.append(node)
        return re

