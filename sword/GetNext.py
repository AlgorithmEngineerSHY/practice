class TreeLinkNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
        self.next = None
class Solution:
    def GetNext(self, pNode):
        if pNode.right:
            return self.helper(pNode.right)
        while pNode.next:
            if pNode.next.left is pNode:
                return pNode.next
            else:
                pNode = pNode.next
        return None

    def helper(self, node):
        if not node.left:
            return node
        else:
            return self.helper(node.left)


