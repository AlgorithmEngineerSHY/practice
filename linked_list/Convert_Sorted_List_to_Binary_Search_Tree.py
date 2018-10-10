'''
Given a singly linked list where elements are sorted in ascending order, 
convert it to a height balanced BST.
For this problem, 
a height-balanced binary tree is defined as a binary tree 
in which the depth of the two subtrees of every node never differ by more than 1.
'''


# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def sortedListToBST(self, head):
        """
        :type head: ListNode
        :rtype: TreeNode
        """
        if not head:
            return None
        if head.next is None:
            return TreeNode(head.val)
        slow, fast = head, head.next.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        root = slow.next
        slow.next = None
        tree_node = TreeNode(root.val)
        tree_node.left = self.sortedListToBST(head)
        tree_node.right = self.sortedListToBST(root.next)

        return tree_node