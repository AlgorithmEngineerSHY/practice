'''
Given a binary tree containing digits from 0-9 only,
each root-to-leaf path could represent a number.
An example is the root-to-leaf path 1->2->3 which represents the number 123.
Find the total sum of all root-to-leaf numbers.
'''


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def __init__(self):
        self.sum = 0
    def sumNumbers(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0
        self.helper(root, '')
        return self.sum

    def helper(self, root, strng):
        if not root.left and not root.right:
            self.sum += int(strng + str(root.val))
            return None
        if root.left:
            self.helper(root.left, strng + str(root.val))
        if root.right:
            self.helper(root.right, strng + str(root.val))
