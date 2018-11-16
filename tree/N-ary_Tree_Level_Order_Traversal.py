
# Definition for a Node.
class Node(object):
    def __init__(self, val, children):
        self.val = val
        self.children = children



class Solution(object):
    def levelOrder(self, root):
        """
        :type root: Node
        :rtype: List[List[int]]
        """
        if not root:
            return []
        res = []
        stack = [root]
        while stack:
            tmp_stack = []
            tmp_val = []
            for node in stack:
                tmp_val.append(node.val)
                if node.children:
                    tmp_stack += node.children
            res.append(tmp_val)
            stack = tmp_stack
        return res


