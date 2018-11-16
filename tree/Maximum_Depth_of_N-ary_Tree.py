
# Definition for a Node.
class Node(object):
    def __init__(self, val, children):
        self.val = val
        self.children = children


class Solution(object):
    def maxDepth(self, root):
        """
        :type root: Node
        :rtype: int
        """
        if not root:
            return 0
        res = 0
        stack = [root]
        while stack:
            res += 1
            tmp_stack = []
            for node in stack:
                if node.children:
                    tmp_stack += node.children
            stack = tmp_stack
        return res
