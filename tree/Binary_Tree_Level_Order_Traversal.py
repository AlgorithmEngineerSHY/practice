# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
from collections import deque
class Solution(object):
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if not root:
            return []
        q = deque()
        q.append(root)
        re = []
        while q:
            n_node = len(q)
            q_tmp = deque()
            re_tmp = []
            for i in range(n_node):
                node = q.pop()
                if node.left:
                    q_tmp.appendleft(node.left)
                if node.right:
                    q_tmp.appendleft(node.right)
                re_tmp.append(node.val)
            q = q_tmp
            re.append(re_tmp)
        return re