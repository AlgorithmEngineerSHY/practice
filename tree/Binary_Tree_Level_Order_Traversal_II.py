# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
from collections import deque
class Solution(object):
    def levelOrderBottom(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if not root:
            return []
        q = deque()
        q.append(root)
        # list_node = [root]
        re = deque()
        while q:
            q_tmp = deque()
            list_tmp = []
            while q:
                node = q.pop()
                if node.left:
                    q_tmp.appendleft(node.left)
                if node.right:
                    q_tmp.appendleft(node.right)
                list_tmp.append(node.val)
            re.appendleft(list_tmp)
            q = q_tmp
        return list(re)

