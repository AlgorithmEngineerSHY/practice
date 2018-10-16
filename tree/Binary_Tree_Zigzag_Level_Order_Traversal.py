# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):

    def zigzagLevelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if not root:
            return []
        stack = [root]
        # -1 is left, 1 is right
        l_or_r = -1
        re = []
        while stack:
            len_stack = len(stack)
            re_tmp = []
            stack_tmp = []
            for i in range(len_stack):
                node = stack.pop()
                re_tmp.append(node.val)
                if l_or_r == 1:
                    if node.right:
                        stack_tmp.append(node.right)
                    if node.left:
                        stack_tmp.append(node.left)
                else:
                    if node.left:
                        stack_tmp.append(node.left)
                    if node.right:
                        stack_tmp.append(node.right)
            re.append(re_tmp)
            stack = stack_tmp
            l_or_r *= -1
        return re


