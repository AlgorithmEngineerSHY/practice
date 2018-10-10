# Definition for binary tree with next pointer.
class TreeLinkNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
        self.next = None

class Solution:
    # @param root, a tree link node
    # @return nothing
    def connect(self, root):
        dummy = TreeLinkNode(0)
        helper = dummy
        while root:
            helper.next = root.left
            if root.left:
                helper = helper.next
            helper.next = root.right
            if root.right:
                helper = helper.next
            if root.next:
                root = root.next
            else:
                root = dummy.next
                helper = dummy
